# Military Vehicle Detection & Tracking

[![CI](https://github.com/YOUR_USERNAME/Military-Vehicle-Detection/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/Military-Vehicle-Detection/actions)


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

**Selected baseline:** `llama-farm/military-labeled-yolo` on Hugging Face.

The dataset is reported as CC0-1.0 and contains 12 classes sourced from DVIDS public-domain imagery. We use a focused 7-class subset for this project:

```text
0 tank
1 apc
2 artillery
3 mlrs
4 military_truck
5 helicopter
6 aircraft
```

The original dataset is about 9.61 GB, so it is **not included in this GitHub repository**. The project includes a downloader/filter script that creates the focused YOLO dataset locally.

Dataset source:
https://huggingface.co/datasets/llama-farm/military-labeled-yolo

Download and prepare:

```bash
pip install -r requirements.txt
python scripts/download_dataset.py --output data/military_vehicle_dataset
```

Then copy `configs/data.example.yaml` to `configs/data.yaml` and set:

```yaml
path: data/military_vehicle_dataset
```

The downloader keeps only the seven classes above and remaps their class IDs.


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

## Advanced workflow

```bash
# 1) Download and prepare the dataset
python scripts/download_dataset.py --output data/military_vehicle_dataset

# 2) Copy the example config
cp configs/data.example.yaml configs/data.yaml

# 3) Validate
python scripts/validate_dataset.py --data configs/data.yaml

# 4) Report class distribution
python scripts/dataset_report.py --data configs/data.yaml

# 5) Train
python scripts/train_advanced.py --config configs/train.yaml

# 6) Evaluate
# edit configs/evaluate.yaml -> model: runs/train/.../weights/best.pt
python scripts/evaluate.py --config configs/evaluate.yaml

# 7) Inference / tracking
# edit configs/inference.yaml or configs/tracking.yaml
python scripts/infer_advanced.py --config configs/inference.yaml
python scripts/track_advanced.py --config configs/tracking.yaml
```

## Status
Professional research starter with dataset acquisition, validation, reproducible training, evaluation, inference, tracking, CI, documentation, and licensing/provenance notes.

