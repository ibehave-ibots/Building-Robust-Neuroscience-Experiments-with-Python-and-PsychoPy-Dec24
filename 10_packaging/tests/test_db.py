import csv
import pytest
from posner.experiment import create_subject_dir


def test_subject_dir_creation(create_temp_subject_dir):
    assert create_temp_subject_dir.exists()


def test_subject_dir_overwriting(create_temp_subject_dir):
    _ = create_subject_dir(create_temp_subject_dir, 1, True)
    with pytest.raises(FileExistsError):
        _ = create_subject_dir(create_temp_subject_dir, 1, False)
