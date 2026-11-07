import pandas as pd
import pytest
from src.eda_statistics import calculate_goal_frequency

def test_goal_frequency():
# Arrange: prepare sample goal data.

    goals = pd.Series([3, 1, 3, 0, 1, 3])

# Act: calculate goal frequencies.
    result = calculate_goal_frequency(goals)

# Assert: verify the expected frequencies.
    assert result.equals(pd.Series(data=[1, 2, 3], index=[0, 1, 3]))