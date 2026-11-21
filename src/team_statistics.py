
def validate_goals(matches):
    # Check for missing values in home and away goal columns.
    if matches["FTHG"].isna().any() or matches["FTAG"].isna().any():
        raise ValueError("Goals cannot be missing.")

    # Check for negative goal values.
    if (matches["FTHG"] < 0).any() or (matches["FTAG"] < 0).any():
        raise ValueError("Goals cannot be negative.")


def calculate_home_stats(matches):
    # Validate the input DataFrame before aggregation.
    validate_goals(matches)

    # Group matches by home team and aggregate goal statistics.
    stats = matches.groupby("HomeTeam").agg(
        matches_played=("FTHG", "size"),
        goals_scored=("FTHG", "sum"),
        goals_conceded=("FTAG", "sum"),
        average_goals=("FTHG", "mean")
    )

    # Return a DataFrame indexed by home team.
    return stats


def calculate_away_stats(matches):
    # Validate the input DataFrame before aggregation.
    validate_goals(matches)

    # Group matches by away team and aggregate goal statistics.
    stats = matches.groupby("AwayTeam").agg(
        matches_played=("FTAG", "size"),
        goals_scored=("FTAG", "sum"),
        goals_conceded=("FTHG", "sum"),
        average_goals=("FTAG", "mean")
    )

    # Return a DataFrame indexed by away team.
    return stats
