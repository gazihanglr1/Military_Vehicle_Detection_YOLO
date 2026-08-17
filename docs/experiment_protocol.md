# Experiment Protocol

## Baseline
- Model: YOLO12n
- Image size: 640
- Seed: 42
- Dataset: military-labeled-yolo focused 7-class subset
- Primary split: train/val supplied by dataset
- Metrics: precision, recall, mAP50, mAP50-95

## Experiment naming
Use:
`<model>_<imgsz>_<epochs>_<dataset-version>_<date>`

Example:
`yolo12n_640_100_mlmyolo_v1_2026-08-17`

## Required record
For every experiment record:
- commit SHA
- dataset revision
- model checkpoint
- GPU/CPU
- Python version
- Ultralytics version
- batch size
- epochs
- augmentation configuration
- best epoch
- precision
- recall
- mAP50
- mAP50-95
- inference latency/FPS if measured

## Evaluation
Do not report only mAP. Include qualitative examples and class-wise metrics.

## Reproducibility
Keep configuration files in Git. Keep large weights and datasets outside ordinary Git history.
