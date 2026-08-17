import argparse
from pathlib import Path
from collections import Counter
import yaml

EXTS = {".jpg",".jpeg",".png",".bmp",".webp"}

def main():
    p = argparse.ArgumentParser(description="Create a compact YOLO dataset report.")
    p.add_argument("--data", default="configs/data.yaml")
    args = p.parse_args()
    cfg_path = Path(args.data).resolve()
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    root = Path(cfg["path"])
    if not root.is_absolute():
        root = (cfg_path.parent / root).resolve()

    names = cfg["names"]
    print("Dataset:", root)
    print("Classes:", names)
    grand_images = grand_labels = 0
    counts = Counter()

    for split in ("train","val","test"):
        rel = cfg.get(split)
        if not rel:
            continue
        img_dir = root / rel
        lab_dir = root / str(rel).replace("images","labels",1)
        images = [x for x in img_dir.rglob("*") if x.suffix.lower() in EXTS] if img_dir.exists() else []
        labels = list(lab_dir.rglob("*.txt")) if lab_dir.exists() else []
        grand_images += len(images)
        grand_labels += len(labels)
        for f in labels:
            for line in f.read_text(encoding="utf-8").splitlines():
                parts=line.split()
                if parts:
                    try:
                        counts[int(parts[0])] += 1
                    except ValueError:
                        pass
        print(f"{split}: images={len(images)} labels={len(labels)}")

    print("Total images:", grand_images)
    print("Total label files:", grand_labels)
    print("Objects by class:")
    for cid, name in names.items():
        print(f"  {cid} ({name}): {counts[int(cid)]}")

if __name__ == "__main__":
    main()
