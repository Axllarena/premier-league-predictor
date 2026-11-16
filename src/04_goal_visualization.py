import pandas as pd
import matplotlib.pyplot as plt
from src.eda_statistics import calculate_goal_frequency
from matplotlib.ticker import MaxNLocator

df = pd.read_csv("data/raw/E0_2526.csv")

home_frequency = calculate_goal_frequency(df["FTHG"])
away_frequency = calculate_goal_frequency(df["FTAG"])

maximum_goals = max(df["FTHG"].max(), df["FTAG"].max())

goal_categories = range(0, maximum_goals + 1)

home_frequency = home_frequency.reindex(goal_categories, fill_value=0)
away_frequency = away_frequency.reindex(goal_categories, fill_value=0)

# Validate frequency totals against the number of matches.
assert home_frequency.sum() == len(df), "Unexpected home frequency total"
assert away_frequency.sum() == len(df), "Unexpected away frequency total"

positions = home_frequency.index.to_numpy()
bar_width = 0.4

fig, ax = plt.subplots()

home_bars = ax.bar(positions - (bar_width/2), home_frequency.values, width=bar_width, label="Home team")
away_bars = ax.bar(positions + (bar_width/2), away_frequency.values, width=bar_width, label="Away team")

ax.bar_label(home_bars, padding=3)
ax.bar_label(away_bars, padding=3)
ax.margins(y=0.10)

ax.set_xlabel("Goals scored")
ax.set_ylabel("Number of matches")
ax.set_title("Premier League 2025/26 - Home vs Away Goals")
ax.set_xticks(positions)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

ax.legend()
plt.show()
