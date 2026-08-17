import argparse
import shutil
from pathlib import Path

from huggingface_hub import snapshot_download

# Original dataset class IDs -> project class IDs.
KEEP = {
    1: 0,  # tank
    2: 1,  # apc
    3: 2,  # artillery
    4: 3,  # mlrs
    5: 4,  # military_truck
    6: 5,  # helicopter
    7: 6,  # aircraft
}

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def process_split(src_root: Path, dst_root: Path, split: str) -> tuple[int, int]:
    src_images = src_root / split / "images"
    src_labels = src_root / split / "labels"
    dst_images = dst_root / "images" / split
    dst_labels = dst_root / "labels" / split
    dst_images.mkdir(parents=True, exist_ok=True)
    dst_labels.mkdir(parents=True, exist_ok=True)

    kept_images = 0
    kept_objects = 0

    for label_path in src_labels.rglob("*.txt"):
        kept_lines = []
        for line in label_path.read_text(encoding="utf-8").splitlines():
            parts = line.split()
            if len(parts) != 5:
                continue
            try:
                original_id = int(parts[0])
            except ValueError:
                continue
            if original_id in KEEP:
                kept_lines.append(" ".join([str(KEEP[original_id]), *parts[1:]]))

        if not kept_lines:
            continue

        rel = label_path.relative_to(src_labels)
        image_path = None
        for ext in IMAGE_EXTS:
            candidate = src_images / rel.with_suffix(ext)
            if candidate.exists():
                image_path = candidate
                break

        if image_path is None:
            continue

        out_image = dst_images / image_path.name
        out_label = dst_labels / f"{image_path.stem}.txt"
        shutil.copy2(image_path, out_image)
        out_label.write_text("\n".join(kept_lines) + "\n", encoding="utf-8")
        kept_images += 1
        kept_objects += len(kept_lines)

    return kept_images, kept_objects


def main():
    p = argparse.ArgumentParser(
        description="Download the CC0 military-labeled YOLO dataset and keep the 7 vehicle/aircraft classes."
    )
    p.add_argument("--output", default="data/military_vehicle_dataset")
    p.add_argument("--revision", default=None)
    p.add_argument("--cache-dir", default=None)
    args = p.parse_args()

    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=True)

    print("Downloading source dataset from Hugging Face.")
    print("The source dataset is approximately 9.6 GB; this can take time and disk space.")

    kwargs = {
        "repo_id": "llama-farm/military-labeled-yolo",
        "repo_type": "dataset",
    }
    if args.revision:
        kwargs["revision"] = args.revision
    if args.cache_dir:
        kwargs["cache_dir"] = args.cache_dir

    src = Path(snapshot_download(**kwargs))

    total_images = total_objects = 0
    for split in ("train", "val"):
        if (src / split).exists():
            images, objects = process_split(src, out, split)
            total_images += images
            total_objects += objects
            print(f"{split}: {images} images, {objects} kept objects")

    print(f"Done. Output: {out}")
    print(f"Total images: {total_images}")
    print(f"Total kept objects: {total_objects}")
    print("Run: python scripts/validate_dataset.py --data configs/data.yaml")


if __name__ == "__main__":
    main()
