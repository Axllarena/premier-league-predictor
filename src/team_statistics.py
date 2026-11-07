def validate_goals(matches):
    # Check for missing goal values.
     if matches["FTHG"].isna().any() or matches["FTAG"].isna().any():
        raise ValueError("Goals cannot be missing.")
    # Check for negative goal values.
     if (matches["FTHG"] < 0).any() or (matches["FTAG"] < 0).any():
        raise ValueError("Goals cannot be negative.")

def calculate_home_stats(matches):

    validate_goals(matches)

    stats = matches.groupby("HomeTeam").agg(
        matches_played=("FTHG", "size"),
        goals_scored=("FTHG", "sum"),
        goals_conceded=("FTAG", "sum"),
        average_goals=("FTHG", "mean")
    )

    return stats

def calculate_away_stats(matches):

    validate_goals(matches)

    stats = matches.groupby("AwayTeam").agg(
        matches_played=("FTAG", "size"),
        goals_scored=("FTAG", "sum"),
        goals_conceded=("FTHG", "sum"),
        average_goals=("FTAG", "mean")
    )

    return stats