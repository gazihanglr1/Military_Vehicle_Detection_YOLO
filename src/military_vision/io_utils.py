from pathlib import Path
import yaml

def load_yaml(path):
    with Path(path).open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def resolve_dataset_path(data_yaml):
    data = load_yaml(data_yaml)
    base = Path(data.get("path", "."))
    if not base.is_absolute():
        base = Path(data_yaml).resolve().parent / base
    return base.resolve()
