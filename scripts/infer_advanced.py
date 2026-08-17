import argparse
from pathlib import Path
import yaml
from ultralytics import YOLO

def main():
    p = argparse.ArgumentParser(description="Run reproducible inference.")
    p.add_argument("--config", default="configs/inference.yaml")
    args = p.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    if not cfg.get("model") or not cfg.get("source"):
        raise SystemExit("Set model and source in configs/inference.yaml")
    model = YOLO(cfg["model"])
    kwargs = {k: v for k, v in cfg.items() if k not in {"model", "device"}}
    if cfg.get("device") != "auto":
        kwargs["device"] = cfg["device"]
    results = model.predict(**kwargs)
    print(f"Processed {len(results)} result item(s).")

if __name__ == "__main__":
    main()
