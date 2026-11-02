def calculate_home_stats(matches):
    stats = matches.groupby("HomeTeam").agg(
        matches_played=("FTHG", "size"),
        goals_scored=("FTHG", "sum"),
        goals_conceded=("FTAG", "sum"),
        average_goals=("FTHG", "mean")
    )

    return stats

def calculate_away_stats(matches):
    stats = matches.groupby("AwayTeam").agg(
        matches_played=("FTAG", "size"),
        goals_scored=("FTAG", "sum"),
        goals_conceded=("FTHG", "sum"),
        average_goals=("FTAG", "mean")
    )

    return stats