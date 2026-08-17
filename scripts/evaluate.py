import argparse
from pathlib import Path
import yaml
from ultralytics import YOLO

def main():
    p = argparse.ArgumentParser(description="Evaluate a trained detector.")
    p.add_argument("--config", default="configs/evaluate.yaml")
    args = p.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    if not cfg.get("model"):
        raise SystemExit("Set model: path/to/best.pt in configs/evaluate.yaml")
    model = YOLO(cfg["model"])
    kwargs = {k: v for k, v in cfg.items() if k != "model" and v is not None}
    if kwargs.get("device") == "auto":
        kwargs.pop("device")
    metrics = model.val(**kwargs)
    print(metrics)

if __name__ == "__main__":
    main()
