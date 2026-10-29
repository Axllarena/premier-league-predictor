
import pandas as pd

# Load historical Premier League match data.
df = pd.read_csv("data/raw/E0_2526.csv")

# Calculate home team statistics.
home_stats = df.groupby("HomeTeam").agg(
    matches_played=("FTHG", "size"),
    goals_scored=("FTHG", "sum"),
    goals_conceded=("FTAG", "sum"),
    average_goals=("FTHG", "mean")
)

# Rank home teams by total goals scored.
home_stats = home_stats.sort_values(
    by="goals_scored",
    ascending=False
)

print("Home team statistics:")
print(home_stats)

# Validate match counts and home goal totals.
print("\nTotal grouped home matches:", home_stats["matches_played"].sum())
print("Total original matches:", len(df))

print("\nTotal grouped home goals:", home_stats["goals_scored"].sum())
print("Total original home goals:", df["FTHG"].sum())


# Calculate away team statistics.

away_stats = df.groupby("AwayTeam").agg(
    matches_played=("FTAG", "size"),
    goals_scored=("FTAG", "sum"),
    goals_conceded=("FTHG", "sum"),
    average_goals=("FTAG", "mean")
)

away_stats = away_stats.sort_values(by="goals_scored", ascending=False)

print("\nAWAY STATS")
print(away_stats)

# Validate away match counts and goal totals.
print("\nTotal grouped away matches:", away_stats["matches_played"].sum())
print("Total original matches:", len(df))

print("\nTotal grouped away goals:", away_stats["goals_scored"].sum())
print("Total original away goals:", df["FTAG"].sum())