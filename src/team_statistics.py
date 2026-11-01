def calculate_home_stats(matches):
    stats = matches.groupby("HomeTeam").agg(
        matches_played=("FTHG", "size"),
        goals_scored=("FTHG", "sum"),
        goals_conceded=("FTAG", "sum"),
        average_goals=("FTHG", "mean")
    )

    return stats