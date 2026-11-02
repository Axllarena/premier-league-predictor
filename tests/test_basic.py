import pandas as pd
import pytest
from src.team_statistics import calculate_home_stats, calculate_away_stats


# Calculate points earned from victories.
def calculate_points(wins):
    return wins * 3


# Verify points for four victories.
def test_calculate_points():
    result = calculate_points(4)
    assert result == 12


# Verify home team statistics.
def test_home_statistics():

    # Arrange: prepare test data.
    matches = pd.DataFrame({
        "HomeTeam": ["Liverpool", "Arsenal", "Liverpool"],
        "FTHG": [2, 1, 4],
        "FTAG": [0, 1, 2]
    })
     # Act: execute the function.
    home_stats = calculate_home_stats(matches)
    # Assert: verify expected results.
    assert home_stats.loc["Liverpool", "matches_played"] == 2
    assert home_stats.loc["Liverpool", "average_goals"] == 3

def test_away_statistics():
    # Arrange: prepare test data.
    matches = pd.DataFrame({
        "HomeTeam": ["Arsenal", "Chelsea", "Liverpool"],
        "AwayTeam": ["Liverpool", "Liverpool", "Arsenal"],
        "FTHG": [1, 2, 4],
        "FTAG": [3, 2, 1],
    })
    # Act: execute the function.
    away_stats = calculate_away_stats(matches)
    # Assert: verify expected results.
    assert away_stats.loc["Liverpool", "matches_played"] == 2
    assert away_stats.loc["Liverpool", "goals_scored"] == 5
    assert away_stats.loc["Liverpool", "goals_conceded"] == 3
    assert away_stats.loc["Liverpool", "average_goals"] == 2.5

def test_home_statistics_zero_goals():

    matches = pd.DataFrame({
    "HomeTeam": ["Liverpool", "Liverpool"],
    "FTHG": [0, 0],
    "FTAG": [1, 2]
    })

    home_stats = calculate_home_stats(matches)

    assert home_stats.loc["Liverpool", "goals_scored"] == 0
    assert home_stats.loc["Liverpool", "goals_conceded"] == 3

def test_home_statistics_empty():

    matches = pd.DataFrame({
        "HomeTeam": [],
        "FTHG": [],
        "FTAG": []

    })

    home_stats = calculate_home_stats(matches)

    assert home_stats.empty

def test_home_statistics_missing_column():
    # Arrange: prepare incomplete data.

    matches = pd.DataFrame({
    "HomeTeam": ["Liverpool"],
    "FTHG": [2]
    })

    # Act and Assert: expect a KeyError.
    with pytest.raises(KeyError):
        calculate_home_stats(matches)


def test_home_statistics_negative_goals():

    matches = pd.DataFrame({
    "HomeTeam": ["Liverpool", "Liverpool"],
    "FTHG": [2, -3],
    "FTAG": [1, 0]
    })

     # Expect a ValueError.
    with pytest.raises(ValueError):
        calculate_home_stats(matches)

def test_away_statistics_negative_goals():
    matches = pd.DataFrame({
        "HomeTeam": ["Arsenal", "Chelsea"],
        "AwayTeam": ["Liverpool", "Liverpool"],
        "FTHG":[2, 1],
        "FTAG":[-1, 3]
    })

    with pytest.raises(ValueError):
        calculate_away_stats(matches)