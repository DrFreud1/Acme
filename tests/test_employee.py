from datetime import time

import pytest

from app.employee import Employee


@pytest.fixture
def mock_raw_shift_data():
    shift_data = "MO09:00-12:00,MO22:00-23:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
    return shift_data


@pytest.fixture
def mock_parsed_shift_data():
    shift_data = {
        "MO": [(time(9, 0), time(12, 0)), (time(22, 0), time(23, 0))],
        "TU": [(time(10, 0), time(12, 0))],
        "TH": [(time(1, 0), time(3, 0))],
        "SA": [(time(14, 0), time(18, 0))],
        "SU": [(time(20, 0), time(21, 0))],
    }
    return shift_data


def test_parse_shift(mock_raw_shift_data, mock_parsed_shift_data):
    parsed_shift = Employee.parse_shift(mock_raw_shift_data)
    assert parsed_shift == mock_parsed_shift_data
