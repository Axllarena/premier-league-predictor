import pandas as pd

df = pd.read_csv("data/raw/E0_2526.csv")

'''print(df.head())

print(df.shape)

print(df["HomeTeam"])

print(df[["HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"]])'''

partidos = df[["HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"]]
print(partidos.head(10))

