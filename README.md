# Premier League Predictor

A Python project focused on exploring English Premier League football data and gradually developing a match outcome prediction system.

The project follows an incremental development approach, emphasizing data analysis, reproducibility, automated testing, and an understanding of the methods used.

## Project Status

**In development — Descriptive analysis and data validation**

The project currently supports historical match data exploration and the calculation of home and away team statistics using Python and Pandas.

Reusable functions have been implemented to aggregate match statistics, including matches played, goals scored, goals conceded, and average goals. Data validation detects missing and negative goal values, and the current implementation includes 10 automated tests using pytest.

**Match outcome prediction models have not yet been implemented.** The current results are descriptive statistics, not predictions.

## Objectives

- Explore and understand historical Premier League match data.
- Learn data analysis techniques using Python and Pandas.
- Develop reliable data processing and validation practices.
- Apply statistical methods to football performance analysis.
- Develop and evaluate match outcome prediction models in future stages.
- Document the development process, decisions, and results.

## Current Features

- Load and explore historical Premier League match data from CSV files.
- Calculate home and away team statistics.
- Aggregate goals scored, goals conceded, matches played, and average goals.
- Combine home and away statistics into a team-level DataFrame.
- Display diagnostic checks for team index uniqueness, team coverage, match counts, and goal totals.
- Detect missing and negative goal values.
- Run automated tests for statistical calculations and selected edge cases.

## Technologies

- Python 3.14
- Pandas 3.0.6
- pytest 9.2.0
- Git and GitHub

## Project Structure

```text
premier-league-predictor/
├── data/
│   └── raw/
│       └── E0_2526.csv
├── src/
│   ├── 01_explore_data.py
│   ├── 02_team_analysis.py
│   └── team_statistics.py
├── tests/
│   └── test_basic.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Getting Started

The following instructions use macOS/Linux terminal commands.

### 1. Create a virtual environment

From the project root:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Explore the dataset

Make sure the historical match dataset is available at `data/raw/E0_2526.csv`.

Run the initial exploration script:

```bash
python src/01_explore_data.py
```

### 4. Run the team analysis

```bash
python -m src.02_team_analysis
```

The script calculates home and away team statistics, combines them into a descriptive team-level dataset, and prints validation summaries.

### 5. Run automated tests

```bash
python -m pytest -v
```

The current test suite contains 10 tests covering basic calculations, home and away statistics, and selected data validation scenarios.

## Current Dataset

The project currently uses historical Premier League match data from the 2025/26 season, stored locally in:

`data/raw/E0_2526.csv`

The dataset contains 380 matches involving 20 teams.

The current analysis verifies the following season totals:

| Metric | Value |
|---|---:|
| Teams | 20 |
| Matches | 380 |
| Home goals | 580 |
| Away goals | 465 |

The data is currently used for descriptive analysis. Full-season aggregates must not be used as pre-match information for fixtures within the same season, as this would introduce temporal data leakage.

## Current Limitations

- The project does not yet predict match outcomes.
- Pre-match features and time-aware evaluation have not yet been implemented.
- The current analysis focuses on a single historical Premier League season.
- Automated tests cover selected calculations and data quality cases, not every possible input.
- No prediction API or deployed application is available.

## Future Development

Planned development areas include:

- Exploratory data analysis and visualizations.
- Applied statistics and probability.
- Data engineering, SQL, and reproducible pipelines.
- Pre-match feature engineering without temporal leakage.
- Baseline prediction models and evaluation.
- Machine learning models for football match outcomes.
- Documentation, reproducibility, and deployment practices.

These features will be developed incrementally and will be documented only when implemented and verified.

## Development

This project is being developed incrementally as a practical learning and portfolio project, with an emphasis on understanding the technical decisions behind each implementation.

The long-term objective is to build a reliable and explainable football analytics project while developing skills in Data Science, Data Engineering, and Machine Learning.