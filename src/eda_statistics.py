
def calculate_goal_frequency(goals):
    goals = goals.value_counts()
    goals = goals.sort_index()

    return goals


def calculate_range_proportion(goals, lower_bound, upper_bound):
    if lower_bound > upper_bound:
        raise ValueError("Lower bound cannot be greater than upper bound")

    if goals.empty:
        raise ValueError("Series is empty")

    if goals.isna().any():
        raise ValueError("Goals contain missing values")

    goals = (goals >= lower_bound) & (goals <= upper_bound)

    return goals.mean()
