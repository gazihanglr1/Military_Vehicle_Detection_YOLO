import argparse
from pathlib import Path
import yaml
from ultralytics import YOLO

def load_yaml(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))

def main():
    p = argparse.ArgumentParser(description="Reproducible YOLO training runner.")
    p.add_argument("--config", default="configs/train.yaml")
    args = p.parse_args()
    cfg = load_yaml(args.config)

    device = cfg.get("device", "auto")
    if device == "auto":
        device = None

    model = YOLO(cfg["model"])
    kwargs = {k: v for k, v in cfg.items() if k not in {"model", "device"}}
    if device is not None:
        kwargs["device"] = device
    model.train(**kwargs)

if __name__ == "__main__":
    main()
