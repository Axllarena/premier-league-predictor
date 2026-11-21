
import pandas as pd

# Load historical Premier League match data.
df = pd.read_csv("data/raw/E0_2526.csv")

# Select the columns needed for match outcome analysis.
matches = df[["HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"]]

# Count matches by result (H = home win, D = draw, A = away win).
outcome_counts = matches["FTR"].value_counts()

# Calculate the percentage of each recorded result.
outcome_percentages = matches["FTR"].value_counts(normalize=True) * 100

# Check for missing or invalid match results.
missing_results = matches["FTR"].isna().sum()
allowed_results = ["H", "D", "A"]
invalid_count = (~matches["FTR"].isin(allowed_results)).sum()

# Display the analysis results.
print("Match outcome counts:")
print(outcome_counts)

print("\nMatch outcome percentages:")
print(outcome_percentages)

print("\nMissing results:", missing_results)
print("Invalid results (including missing):", invalid_count)

print("Dataset shape (rows, columns):", df.shape)
