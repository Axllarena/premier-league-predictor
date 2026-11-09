
import pandas as pd

from src.eda_statistics import (
    calculate_goal_frequency,
    calculate_range_proportion,
)


# Load Premier League match data.
df = pd.read_csv("data/raw/E0_2526.csv")

# Calculate the absolute frequency of home goals.
home_goal_frequency = calculate_goal_frequency(df["FTHG"])

# Reconstruct total home goals from the frequency distribution.
goal_values = home_goal_frequency.index.to_numpy()
total_home_goals = (home_goal_frequency.values * goal_values).sum()

# Validate the reconstructed total.
assert total_home_goals == df["FTHG"].sum(), "Unexpected number of home goals"

# Calculate and validate relative frequencies.
home_goal_relative_frequency = df["FTHG"].value_counts(
    normalize=True
).sort_index()

assert round(home_goal_relative_frequency.sum(), 2) == 1.0, (
    "Invalid relative frequency total"
)

# Method A: Calculate proportions from the frequency distribution.
at_least_two_frequency = home_goal_relative_frequency[
    home_goal_relative_frequency.index >= 2
].sum()

at_most_one_frequency = home_goal_relative_frequency[
    home_goal_relative_frequency.index <= 1
].sum()

# Method B: Calculate proportions directly from match data.
at_least_two_home_goals = (df["FTHG"] >= 2).mean()
at_most_one_home_goal = (df["FTHG"] <= 1).mean()

# Calculate the proportion of matches with 2 to 4 home goals.
home_goals_in_range_proportion = calculate_range_proportion(
    df["FTHG"], 2, 4
)

# Calculate the proportion of matches with zero or at least four home goals.
zero_or_four_plus_home_goals_proportion = (
    (df["FTHG"] == 0) | (df["FTHG"] >= 4)
).mean()

# Apply the reusable function to away goals.
away_goals_in_range_proportion = calculate_range_proportion(
    df["FTAG"], 1, 3
)

# Verify that both methods produce the same proportions.
assert round(at_least_two_frequency, 6) == round(at_least_two_home_goals, 6)
assert round(at_most_one_frequency, 6) == round(at_most_one_home_goal, 6)

# Verify that complementary events cover all matches.
assert round(at_least_two_home_goals + at_most_one_home_goal, 6) == 1.0

# Display the results.
print("Home goal frequency:")
print(home_goal_frequency)

print("\nHome goal relative frequency:")
print(home_goal_relative_frequency)

print(
    "\nProportion of matches with at least two home goals:",
    at_least_two_home_goals,
)
print(
    "Proportion of matches with at most one home goal:",
    at_most_one_home_goal,
)
print(
    "Proportion of matches with 2 to 4 home goals:",
    home_goals_in_range_proportion,
)
print(
    "Proportion of matches with zero or at least four home goals:",
    zero_or_four_plus_home_goals_proportion,
)
print(
    "Proportion of matches with 1 to 3 away goals:",
    away_goals_in_range_proportion,
)
