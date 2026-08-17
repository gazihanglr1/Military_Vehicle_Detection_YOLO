import argparse
from src.military_vision.detector import load_model, predict

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True)
    p.add_argument("--source", required=True)
    p.add_argument("--conf", type=float, default=0.25)
    p.add_argument("--imgsz", type=int, default=640)
    a = p.parse_args()
    predict(load_model(a.model), a.source, conf=a.conf, imgsz=a.imgsz)

if __name__ == "__main__":
    main()
