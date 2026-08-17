import argparse
from pathlib import Path
import yaml
from PIL import Image

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", required=True)
    a = p.parse_args()
    data_path = Path(a.data).resolve()
    data = yaml.safe_load(data_path.read_text(encoding="utf-8"))
    root = Path(data["path"])
    if not root.is_absolute():
        root = (data_path.parent / root).resolve()
    n_classes = len(data["names"])
    errors = []
    total_images = total_labels = 0

    for split in ("train", "val", "test"):
        rel = data.get(split)
        if not rel:
            continue
        image_dir = root / rel
        label_dir = root / str(rel).replace("images", "labels", 1)
        if not image_dir.exists():
            errors.append(f"{split}: missing {image_dir}")
            continue
        images = [x for x in image_dir.rglob("*") if x.suffix.lower() in
                  {".jpg",".jpeg",".png",".bmp",".webp"}]
        for image_path in images:
            total_images += 1
            try:
                with Image.open(image_path) as im:
                    im.verify()
            except Exception as exc:
                errors.append(f"Unreadable image {image_path}: {exc}")
                continue
            label_path = label_dir / f"{image_path.stem}.txt"
            if not label_path.exists():
                errors.append(f"Missing label for {image_path}")
                continue
            total_labels += 1
            for line_no, line in enumerate(label_path.read_text().splitlines(), 1):
                parts = line.split()
                if len(parts) != 5:
                    errors.append(f"{label_path}:{line_no}: expected 5 values")
                    continue
                try:
                    cls = int(parts[0]); vals = [float(x) for x in parts[1:]]
                except ValueError:
                    errors.append(f"{label_path}:{line_no}: non-numeric value")
                    continue
                if not 0 <= cls < n_classes:
                    errors.append(f"{label_path}:{line_no}: class id out of range")
                if any(v < 0 or v > 1 for v in vals):
                    errors.append(f"{label_path}:{line_no}: bbox outside [0,1]")

    print(f"Images checked: {total_images}")
    print(f"Images with labels found: {total_labels}")
    print(f"Errors: {len(errors)}")
    for e in errors[:100]:
        print("ERROR:", e)
    raise SystemExit(1 if errors else 0)

if __name__ == "__main__":
    main()
