
def calculate_goal_frequency(goals):
    # Convert the input Series into a frequency distribution.
    goals = goals.value_counts()

    # Sort the resulting Series by goal count (index).
    goals = goals.sort_index()

    return goals


def calculate_range_proportion(goals, lower_bound, upper_bound):
    # Validate interval bounds and input Series.
    if lower_bound > upper_bound:
        raise ValueError("Lower bound cannot be greater than upper bound")

    if goals.empty:
        raise ValueError("Series is empty")

    if goals.isna().any():
        raise ValueError("Goals contain missing values")

    # Create a boolean Series indicating which goals fall within the inclusive range.
    goals = (goals >= lower_bound) & (goals <= upper_bound)

    # Return the proportion of True values as a float.
    return goals.mean()
