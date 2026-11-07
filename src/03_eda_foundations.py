import pandas as pd
from src.eda_statistics import calculate_goal_frequency

df = pd.read_csv("data/raw/E0_2526.csv")

# Explore the distribution of home goals per match.

goals_hometeam_frequency = calculate_goal_frequency(df["FTHG"])

print(goals_hometeam_frequency)

# Reconstruct total home goals from the frequency distribution.

goals_count = goals_hometeam_frequency.index.to_numpy()

total_home_goals = (goals_hometeam_frequency.values * goals_count).sum()

print(total_home_goals)

# Verify that reconstructed home goals match the original dataset.

assert total_home_goals == df["FTHG"].sum(), "Unexpected number of goals"
