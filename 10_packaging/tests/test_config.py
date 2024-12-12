import pytest
from posner.experiment import load_config, Config
from pydantic import ValidationError


def test_load_config(write_config):
    config_fname = write_config
    load_config(config_fname)


def test_config_not_found():
    with pytest.raises(FileNotFoundError):
        load_config("")


def test_missing_key_is_detected(config_dict):
    for key in config_dict.keys():
        wrong_config = config_dict.copy()
        print(key)
        del wrong_config[key]
        with pytest.raises(ValidationError):
            Config(**wrong_config)


def test_wrong_types_are_detected(config_dict):
    for key, value in zip(
        ["fix_dur", "cue_dur", "n_blocks", "n_trials"], ["hi", -2, 0.5, 19]
    ):
        wrong_config = config_dict.copy()
        wrong_config[key] = value
        with pytest.raises(ValidationError):
            Config(**wrong_config)

