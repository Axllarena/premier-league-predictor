
def calculate_goal_frequency(goals):
    goals = goals.value_counts()
    goals = goals.sort_index()
    
    return goals