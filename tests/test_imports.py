def test_imports():
    from src.military_vision.detector import load_model, predict, track
    from src.military_vision.io_utils import load_yaml, resolve_dataset_path
    assert callable(load_model)
    assert callable(predict)
    assert callable(track)
    assert callable(load_yaml)
    assert callable(resolve_dataset_path)
