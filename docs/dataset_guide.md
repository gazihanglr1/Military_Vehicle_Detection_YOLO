# Dataset Guide

## Selected baseline

`llama-farm/military-labeled-yolo`

Source:
https://huggingface.co/datasets/llama-farm/military-labeled-yolo

The dataset card reports CC0-1.0 and DVIDS public-domain imagery. The full source is about 9.61 GB.

## Project subset

We keep:

| New ID | Class | Original ID |
|---:|---|---:|
| 0 | tank | 1 |
| 1 | apc | 2 |
| 2 | artillery | 3 |
| 3 | mlrs | 4 |
| 4 | military_truck | 5 |
| 5 | helicopter | 6 |
| 6 | aircraft | 7 |

We intentionally leave out soldier, warship, missile_launcher, car and generic truck for this first vehicle/aircraft-focused baseline.

## Why this dataset?

- multi-class military object detection;
- YOLO-format annotations;
- DVIDS-sourced public-domain imagery according to its dataset card;
- CC0-1.0 is stated for the dataset;
- enough variety to establish a useful baseline.

## Important

Do not copy the dataset into the GitHub repository. Use the downloader and cite the dataset source. Re-check the dataset card/license before redistribution or commercial use.
