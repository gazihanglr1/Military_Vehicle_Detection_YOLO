# Military Vehicle Detection

Independent computer-vision project for detecting and tracking military vehicles in images and video using Ultralytics YOLO.

**Reference:** Orion by Jonas Renault was reviewed for the general workflow (dataset preparation -> training -> evaluation -> video detection/tracking). No Orion source code is included here.

## Scope
General-purpose visual object detection and multi-object tracking for research/education. No weapon guidance, fire-control, engagement, or autonomous targeting functionality.

## Pipeline
Dataset -> validation/preparation -> YOLO training -> evaluation -> image/video inference -> multi-object tracking -> results

## Structure
- `configs/` dataset configuration
- `scripts/` training, prediction, tracking, validation
- `src/military_vision/` reusable Python code
- `docs/` methodology and dataset guidance
- `data/` dataset instructions
- `models/` model-weight instructions
- `examples/` redistributable demo media
- `tests/` basic tests

## Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:
```powershell
.venv\Scripts\activate
pip install -r requirements.txt
```

## Dataset
Copy `configs/data.example.yaml` to `configs/data.yaml` and edit it.

Expected YOLO layout:
```text
dataset/
  images/train
  images/val
  images/test
  labels/train
  labels/val
  labels/test
```

## Commands
Validate:
```bash
python scripts/validate_dataset.py --data configs/data.yaml
```

Train:
```bash
python scripts/train.py --model yolo12n.pt --data configs/data.yaml --epochs 100 --imgsz 640
```

Predict:
```bash
python scripts/predict.py --model path/to/best.pt --source path/to/image.jpg
```

Track:
```bash
python scripts/track.py --model path/to/best.pt --source path/to/video.mp4
```

## Reproducibility
Record dataset name/version/license, class list, splits, model, image size, epochs, batch, hardware, Python version, Ultralytics version, and evaluation metrics.

## Licensing
This starter uses the Ultralytics YOLO ecosystem and is therefore prepared for AGPL-3.0 distribution. See `LICENSE` and verify current third-party terms before deployment. Commercial, closed-source, embedded, or proprietary use may require an Ultralytics Enterprise license.

## References
- Ultralytics: https://github.com/ultralytics/ultralytics
- YOLO12: https://docs.ultralytics.com/models/yolo12
- Orion: https://github.com/jonasrenault/orion

Orion is MIT licensed and is referenced only for project direction/workflow; its source is not copied into this repository.

## Status
Starter repository. Dataset, experiments, trained weights, metrics, and example results are added as the project develops.
