import argparse
from ultralytics import YOLO

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="yolo12n.pt")
    p.add_argument("--data", required=True)
    p.add_argument("--epochs", type=int, default=100)
    p.add_argument("--imgsz", type=int, default=640)
    p.add_argument("--batch", type=int, default=-1)
    p.add_argument("--device", default=None)
    p.add_argument("--project", default="runs/train")
    p.add_argument("--name", default="military_vehicle")
    a = p.parse_args()

    model = YOLO(a.model)
    kwargs = dict(data=a.data, epochs=a.epochs, imgsz=a.imgsz, batch=a.batch,
                  project=a.project, name=a.name)
    if a.device:
        kwargs["device"] = a.device
    model.train(**kwargs)

if __name__ == "__main__":
    main()
