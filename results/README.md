# Results

## YOLO12n baseline

Evaluation metrics supplied by the project author from the validation run:

| Metric | Score |
|---|---:|
| Precision | 0.92 |
| Recall | 0.88 |
| mAP@50 | 0.90 |
| mAP@50-95 | 0.68 |

These values are reported for the project's initial YOLO12n baseline. They should be reproduced from the exact dataset revision, software versions, hardware and training configuration before being treated as a publication-grade benchmark.

### Interpretation

The baseline has strong detection precision/recall and a high mAP@50. The lower mAP@50-95 indicates that localization quality decreases under stricter IoU thresholds. Class-wise metrics and an independent test split are recommended before making stronger generalization claims.

### Reproduce

1. Download the dataset with `scripts/download_dataset.py`.
2. Validate it with `scripts/validate_dataset.py`.
3. Train using `configs/train.yaml`.
4. Evaluate `best.pt` using `scripts/evaluate.py`.
5. Record the exact environment and commit SHA.

Large model weights and generated training artifacts are intentionally excluded from Git history.
