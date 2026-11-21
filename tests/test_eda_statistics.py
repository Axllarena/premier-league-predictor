import pandas as pd
import pytest
from src.eda_statistics import calculate_goal_frequency
from src.eda_statistics import calculate_range_proportion
from src.eda_statistics import calculate_goal_dispersion


def test_goal_frequency():
    # Arrange: prepare sample goal data.

    goals = pd.Series([3, 1, 3, 0, 1, 3])

# Act: calculate goal frequencies.
    result = calculate_goal_frequency(goals)

# Assert: verify the expected frequencies.
    assert result.equals(pd.Series(data=[1, 2, 3], index=[0, 1, 3]))


def test_range_proportion():
    # Arrange: prepare sample goal data.
    goals = pd.Series([0, 2, 3, 4, 5, 2, 1, 3])

    lower_bound = 2
    upper_bound = 4

    # Act: calculate goals proportion.
    result = calculate_range_proportion(goals, lower_bound, upper_bound)

    # Assert: verify the expected proportion.
    assert result == 0.625, "Error: nexpected proportion"


def test_range_proportion_equal_bounds():

    goals = pd.Series([0, 1, 0, 3])

    lower_bound = 0
    upper_bound = 0

    result = calculate_range_proportion(goals, lower_bound, upper_bound)

    assert result == 0.5, "Error: unexpected result"


def test_range_proportion_invalid_bounds():

    goals = pd.Series([0, 2, 4, 5])

    lower_bound = 5
    upper_bound = 2

    with pytest.raises(ValueError):
        calculate_range_proportion(goals, lower_bound, upper_bound)


def test_range_proportion_empty_series():

    goals = pd.Series([], dtype=int)

    lower_bound = 2
    upper_bound = 4

    with pytest.raises(ValueError):
        calculate_range_proportion(goals, lower_bound, upper_bound)


def test_range_proportion_missing_goals():

    goals = pd.Series([1, 2, None, 4])

    lower_bound = 2
    upper_bound = 4

    with pytest.raises(ValueError):
        calculate_range_proportion(goals, lower_bound, upper_bound)


def test_range_proportion_no_matches():
    goals = pd.Series([0, 1, 2, 3, 4])

    lower_bound = 6
    upper_bound = 8

    result = calculate_range_proportion(goals, lower_bound, upper_bound)

    assert result == 0, "Unexpected error"

def test_goal_dispersion():

    # Arrange: prepare sample goal data.
    goals = pd.Series([0, 0, 2, 4, 4])

    # Act: calculate dispersion statistics.
    result = calculate_goal_dispersion(goals)

    # Assert: verify the expected dispersion values.
    assert result["range"] == 4, "Unexpected range"
    assert result["variance"] == pytest.approx(3.2)
    assert result["std_dev"] == pytest.approx(1.7888543819998317)
    assert result["cv"] == pytest.approx(89.442719)

def test_goal_dispersion_constant_values():
    # Arrange: prepare constant goal data.
    goals = pd.Series([2, 2, 2, 2])

    # Act: calculate dispersion statistics.
    result = calculate_goal_dispersion(goals)

    # Assert: verify that all dispersion values are zero.
    assert result["range"] == 0, "Unexpected range"
    assert result["variance"] == 0
    assert result["std_dev"] == 0
    assert result["cv"] == 0

def test_goal_dispersion_empty_series():
    # Arrange: prepare an empty Series.
    goals = pd.Series([], dtype=float)

    # Act & Assert: verify that an empty Series raises ValueError.
    with pytest.raises(ValueError):
        calculate_goal_dispersion(goals)

def test_goal_dispersion_missing_values():
    # Arrange: prepare goal data with a missing value.
    goals = pd.Series([1, 2, None, 4])

    # Act & Assert: verify that missing values raise ValueError.
    with pytest.raises(ValueError):
        calculate_goal_dispersion(goals)

def test_goal_dispersion_zero_mean():
    goals = pd.Series([0, 0, 0, 0])

    result = calculate_goal_dispersion(goals)

    assert result["cv"] is None, "Unexpected error"
    assert result["std_dev"] == 0
