# Military Vehicle Detection & Tracking

A reproducible computer-vision research project for detecting and tracking military vehicles and aircraft in image/video data using Ultralytics YOLO.

> **Research scope:** general visual object detection and multi-object tracking. This repository does not implement weapon guidance, fire-control, engagement decisions, autonomous targeting, or target selection.

[![CI](https://github.com/gazihanglr1/Military_Vehicle_Detection_YOLO/actions/workflows/ci.yml/badge.svg)](https://github.com/gazihanglr1/Military_Vehicle_Detection_YOLO/actions)

## Highlights

- YOLO12-based object detection baseline
- Seven-class military vehicle/aircraft taxonomy
- Automated dataset download and class filtering
- YOLO annotation validation
- Class-distribution reporting
- Reproducible training/evaluation configurations
- Image inference
- Multi-object video tracking with ByteTrack
- CI tests
- Experiment/release documentation
- Dataset provenance and licensing notes

## Pipeline

```text
Dataset
   ↓
Download / class filtering
   ↓
YOLO dataset validation
   ↓
Training
   ↓
Evaluation
   ↓
Image inference
   ↓
Video detection + tracking
   ↓
Results / error analysis
```

## Project Structure

```text
configs/       Training, evaluation, inference and tracking configs
scripts/       CLI utilities and experiment runners
src/           Reusable Python modules
docs/          Methodology, dataset, experiments and release notes
data/          Dataset instructions; large datasets are not committed
models/        Model-weight instructions
examples/      Small redistributable demo-media instructions
results/       Compact reported metrics; generated artifacts are not committed
tests/         Automated tests
.github/       CI and issue templates
```

## Dataset

The baseline uses `llama-farm/military-labeled-yolo` from Hugging Face. Its dataset card reports a CC0-1.0 license and DVIDS-sourced public-domain imagery. The full dataset is approximately 9.61 GB and is intentionally **not** stored in this repository.

Source:
https://huggingface.co/datasets/llama-farm/military-labeled-yolo

### Project classes

| ID | Class |
|---:|---|
| 0 | tank |
| 1 | apc |
| 2 | artillery |
| 3 | mlrs |
| 4 | military_truck |
| 5 | helicopter |
| 6 | aircraft |

The downloader keeps these classes and remaps their IDs into the project taxonomy. Always re-check the source dataset card and license before redistribution or commercial use.

## Installation

```bash
git clone https://github.com/gazihanglr1/Military_Vehicle_Detection_YOLO.git
cd Military_Vehicle_Detection_YOLO

python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Dataset Preparation

```bash
python scripts/download_dataset.py --output data/military_vehicle_dataset
```

Then:

```bash
cp configs/data.example.yaml configs/data.yaml
```

On Windows, copy the file manually if `cp` is unavailable.

Set:

```yaml
path: data/military_vehicle_dataset
```

Validate:

```bash
python scripts/validate_dataset.py --data configs/data.yaml
```

Report class distribution:

```bash
python scripts/dataset_report.py --data configs/data.yaml
```

Expected structure:

```text
data/military_vehicle_dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

## Training

Recommended reproducible baseline:

```bash
python scripts/train_advanced.py --config configs/train.yaml
```

The baseline configuration uses YOLO12n, 640px input, seed 42, automatic batch sizing and conservative augmentations.

After training, the main artifact is:

```text
runs/train/.../weights/best.pt
```

Do not commit large model weights to ordinary Git history.

## Evaluation

Set the model path in:

```text
configs/evaluate.yaml
```

Then:

```bash
python scripts/evaluate.py --config configs/evaluate.yaml
```

## Inference

Set `model` and `source` in:

```text
configs/inference.yaml
```

Run:

```bash
python scripts/infer_advanced.py --config configs/inference.yaml
```

## Tracking

Set `model` and `source` in:

```text
configs/tracking.yaml
```

Run:

```bash
python scripts/track_advanced.py --config configs/tracking.yaml
```

The tracking pipeline uses ByteTrack through the Ultralytics interface.

## Baseline Results

The initial YOLO12n validation run reported:

| Metric | Score |
|---|---:|
| Precision | **0.92** |
| Recall | **0.88** |
| mAP@50 | **0.90** |
| mAP@50-95 | **0.68** |

These values are recorded as the project's initial baseline and should be reproduced from the exact dataset/software environment before being used as a formal benchmark.

The gap between mAP@50 and mAP@50-95 suggests that localization quality becomes more challenging at stricter IoU thresholds. Class-wise metrics, an independent test set and an FPS/latency benchmark are the next recommended experiments.

See [`results/README.md`](results/README.md).

## Reproducibility

For every experiment record:

- Git commit SHA
- dataset name/version/revision
- dataset license
- class mapping
- model/checkpoint
- Python version
- Ultralytics version
- GPU/CPU
- image size
- batch size
- epochs
- augmentation configuration
- precision
- recall
- mAP@50
- mAP@50-95
- inference latency/FPS where measured

See [`docs/experiment_protocol.md`](docs/experiment_protocol.md).

## Limitations

- Dataset quality and annotation noise can affect reported metrics.
- Domain shift is expected between public-domain training imagery and unseen imagery.
- Small, distant or occluded objects may be difficult to detect.
- Validation metrics alone do not establish real-world operational reliability.
- No independent test-set result is claimed yet.
- No FPS/latency claim is made until it is measured on specified hardware.

## References

- YOLO12: https://docs.ultralytics.com/models/yolo12
- Ultralytics: https://github.com/ultralytics/ultralytics
- Orion: https://github.com/jonasrenault/orion
- Dataset: https://huggingface.co/datasets/llama-farm/military-labeled-yolo

Orion was reviewed for general workflow/project direction; no Orion source code is included here.

See [`docs/references.md`](docs/references.md) for citation details.

## Licensing

This repository is prepared for AGPL-3.0 distribution because it uses the Ultralytics YOLO ecosystem. Ultralytics currently documents AGPL-3.0 and an Enterprise licensing route; commercial/closed-source use may require an appropriate Enterprise license. Review the current Ultralytics licensing terms before deployment.

The dataset has its own separate provenance and license terms; see the dataset card before reuse.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Security

Do not commit credentials, private URLs, sensitive imagery, classified material or restricted operational data.

See [`SECURITY.md`](SECURITY.md).

## Release Status

**v1.0.0 — reproducible research baseline**

The repository includes dataset preparation, validation, training, evaluation, inference, tracking, testing, documentation, provenance and baseline metrics. Independent test-set evaluation and hardware benchmark results remain future experimental work and are intentionally not fabricated.
