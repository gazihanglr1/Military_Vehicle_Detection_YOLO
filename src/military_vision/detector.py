from pathlib import Path
from ultralytics import YOLO

def load_model(model_path: str | Path) -> YOLO:
    return YOLO(str(model_path))

def predict(model, source, conf=0.25, imgsz=640, save=True, project="results/detection"):
    return model.predict(source=str(source), conf=conf, imgsz=imgsz, save=save, project=project)

def track(model, source, conf=0.25, imgsz=640, tracker="bytetrack.yaml", save=True, project="results/tracking"):
    return model.track(source=str(source), conf=conf, imgsz=imgsz, tracker=tracker,
                      persist=True, save=save, project=project)
