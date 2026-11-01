import pandas as pd
from src.team_statistics import calculate_home_stats


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

    home_stats = calculate_home_stats(matches)

    # Assert: verify expected results.
    assert home_stats.loc["Liverpool", "matches_played"] == 2
    assert home_stats.loc["Liverpool", "average_goals"] == 3