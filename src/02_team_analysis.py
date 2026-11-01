import pandas as pd
from src.team_statistics import calculate_home_stats

# Load historical Premier League match data.
df = pd.read_csv("data/raw/E0_2526.csv")

# Calculate home team statistics.
home_stats = calculate_home_stats(df)

# Calculate away team statistics.
away_stats = df.groupby("AwayTeam").agg(
    matches_played=("FTAG", "size"),
    goals_scored=("FTAG", "sum"),
    goals_conceded=("FTHG", "sum"),
    average_goals=("FTAG", "mean")
)

# Validate team indexes and check for missing teams.
print("Home team index is unique:", home_stats.index.is_unique)
print("Away team index is unique:", away_stats.index.is_unique)

missing_home = away_stats.index.difference(home_stats.index)
missing_away = home_stats.index.difference(away_stats.index)

print("Teams missing from home stats:", missing_home)
print("Teams missing from away stats:", missing_away)

# Prepare statistics for merging.
home_table = home_stats.reset_index()
away_table = away_stats.reset_index()

# Merge home and away statistics by team.
team_stats = home_table.merge(
    away_table,
    left_on="HomeTeam",
    right_on="AwayTeam",
    how="inner",
    suffixes=("_home", "_away"),
    validate="one_to_one"
)

# Rank teams by home goals scored.
team_stats = team_stats.sort_values(
    by="goals_scored_home",
    ascending=False
)

print("\nTeam statistics:")
print(team_stats)

# Validate match counts and goal totals.
print("\nTotal teams:", len(team_stats))
print("Total home matches:", team_stats["matches_played_home"].sum())
print("Total away matches:", team_stats["matches_played_away"].sum())

print("\nGrouped home goals:", team_stats["goals_scored_home"].sum())
print("Original home goals:", df["FTHG"].sum())

print("\nGrouped away goals:", team_stats["goals_scored_away"].sum())
print("Original away goals:", df["FTAG"].sum())
