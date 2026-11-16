# Premier League Predictor

A Python project focused on exploring English Premier League football data and gradually developing a match outcome prediction system.

The project follows an incremental development approach, emphasizing data analysis, statistical reasoning, reproducibility, automated testing, and a clear understanding of the methods used.

## Project Status

**In development — Exploratory Data Analysis (EDA)**

The project currently supports historical Premier League match data exploration, home and away team statistics, descriptive statistical analysis, and goal distribution visualizations using Python, Pandas, and Matplotlib.

Reusable functions have been implemented to calculate team-level statistics, goal frequencies, proportions, and dispersion measures. Data validation detects selected invalid inputs, including missing and negative goal values where applicable.

The implementation currently includes **22 automated tests using pytest**, covering statistical calculations, data validation, and selected edge cases.

A grouped bar chart comparing home and away goal frequencies has also been implemented, including numerical value labels for improved readability.

**Match outcome prediction models have not yet been implemented.** The current results are descriptive statistics, not predictions.

## Objectives

- Explore and understand historical Premier League match data.
- Develop practical data analysis skills using Python and Pandas.
- Apply descriptive statistical methods to football performance analysis.
- Analyze goal frequencies, distributions, and variability.
- Create clear and interpretable football data visualizations.
- Develop reliable, reusable, and testable data processing functions.
- Apply data validation and software engineering best practices.
- Investigate potential relationships relevant to future predictive modeling.
- Develop and evaluate match outcome prediction models in future stages.
- Document the development process, technical decisions, limitations, and findings.

## Current Features

### Data Exploration and Validation

- Load and explore historical Premier League match data from CSV files.
- Inspect dataset dimensions, columns, and match results.
- Identify missing values and selected invalid data.
- Validate goal statistics and match totals.
- Detect missing and negative goal values in team statistics processing.

### Team Statistics

- Calculate home and away team statistics.
- Aggregate matches played, goals scored, goals conceded, and average goals.
- Combine home and away statistics into a team-level DataFrame.
- Validate team index uniqueness and team coverage.
- Verify match counts and goal totals.

### Exploratory Data Analysis

- Calculate absolute and relative goal frequencies.
- Identify goal distribution patterns and modal values.
- Calculate match proportions within specified goal ranges.
- Apply Boolean conditions to analyze goal counts.
- Calculate descriptive statistics, including:
  - Mean.
  - Range.
  - Population variance.
  - Population standard deviation.
  - Coefficient of variation.
- Compare absolute and relative goal variability between home and away teams.
- Handle undefined coefficients of variation when the mean is zero.
- Validate statistical functions against empty inputs and missing values.

### Data Visualization

- Create grouped bar charts using Matplotlib.
- Compare home and away goal frequency distributions.
- Display exact frequency values above bars.
- Configure axes, legends, labels, and chart spacing.
- Improve the readability and interpretation of statistical results.

### Automated Testing

- Execute automated tests using pytest.
- Validate team-level statistical calculations.
- Verify goal frequencies, proportions, and dispersion measures.
- Test selected edge cases and invalid inputs.
- Compare floating-point results using approximate assertions.

**Current test suite: 22 passing tests.**

## Technologies

- Python 3.14
- Pandas 3.0.6
- Matplotlib 3.11.2
- pytest 9.2.0
- Git and GitHub
- Visual Studio Code

## Project Structure

```text
premier-league-predictor/
├── data/
│   └── raw/
│       └── E0_2526.csv
├── src/
│   ├── 01_explore_data.py
│   ├── 02_team_analysis.py
│   ├── 03_eda_foundations.py
│   ├── 04_goal_visualization.py
│   ├── eda_statistics.py
│   └── team_statistics.py
├── tests/
│   ├── test_basic.py
│   └── test_eda_statistics.py
├── .gitignore
├── README.md
└── requirements.txt
```

### Main Files

- `01_explore_data.py`: Initial dataset exploration and inspection.
- `02_team_analysis.py`: Home and away team statistics analysis.
- `03_eda_foundations.py`: Descriptive statistical analysis of goal distributions.
- `04_goal_visualization.py`: Goal distribution visualization with Matplotlib.
- `eda_statistics.py`: Reusable statistical functions for goal analysis.
- `team_statistics.py`: Reusable team statistics calculations and validation.
- `test_basic.py`: Tests for foundational calculations and team statistics.
- `test_eda_statistics.py`: Tests for EDA statistics and selected edge cases.

## Getting Started

The following instructions use macOS/Linux terminal commands.

### 1. Create a Virtual Environment

From the project root:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Explore the Dataset

Make sure the historical match dataset is available at:

`data/raw/E0_2526.csv`

Run the initial exploration script:

```bash
python src/01_explore_data.py
```

### 4. Run the Team Analysis

```bash
python -m src.02_team_analysis
```

The script calculates home and away team statistics, combines them into a descriptive team-level dataset, and prints validation summaries.

### 5. Run Exploratory Data Analysis

```bash
python -m src.03_eda_foundations
```

This module calculates and displays descriptive statistics for home and away goals, including frequencies, proportions, and dispersion measures.

The analysis includes the coefficient of variation to compare relative variability between distributions with different means.

### 6. Generate Goal Distribution Visualizations

```bash
python -m src.04_goal_visualization
```

The script generates a grouped bar chart comparing the frequency of goals scored by home and away teams.

Each bar includes a numerical label representing the corresponding number of matches.

### 7. Run Automated Tests

```bash
python -m pytest -v
```

Alternatively, run the suite with concise output:

```bash
python -m pytest -q
```

The current test suite contains **22 tests** covering foundational calculations, team statistics, descriptive EDA statistics, and selected validation scenarios.

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
| Total goals | 1,045 |

The dataset includes match-level information such as home and away teams, goals scored, and final match results.

The data is currently used for descriptive analysis.

**Important:** Full-season aggregates must not be used as pre-match information for fixtures within the same season, as this would introduce temporal data leakage.

Future predictive features must be calculated using only information available before each match.

## Exploratory Data Analysis

### Purpose

The purpose of this exploratory data analysis is to examine the distribution of goals scored by home and away teams across the 380 matches of the 2025/26 Premier League season.

The analysis aims to identify differences in goal frequencies, averages, and variability through descriptive statistics and data visualizations.

These findings will help us better understand the dataset and guide future decisions in developing the match outcome prediction system.

### Methods

The exploratory data analysis was conducted using Pandas to process and analyze match data from the 2025/26 Premier League season.

Absolute and relative goal frequencies were calculated separately for home and away teams.

Descriptive statistics, including the mean, range, population variance, population standard deviation, and coefficient of variation, were used to examine and compare goal distributions.

The population variance and standard deviation were calculated using `ddof=0` to describe the complete set of matches in the analyzed season.

The coefficient of variation was calculated as:

```text
CV = (Population Standard Deviation / Mean) × 100
```

When the mean is zero, the coefficient of variation is treated as undefined and represented by `None`, while the remaining statistics are preserved.

Matplotlib was used to create a grouped bar chart comparing the number of matches associated with each goal count for home and away teams.

Numerical labels were added to improve readability and facilitate comparisons between both distributions.

### Descriptive Statistics

The following statistics summarize the observed goal distributions:

| Statistic | Home Goals | Away Goals |
|---|---:|---:|
| Total goals | 580 | 465 |
| Mean goals | 1.53 | 1.22 |
| Goal range | 5 | 5 |
| Population variance | 1.3651 | 1.1736 |
| Population standard deviation | 1.1684 | 1.0834 |
| Coefficient of variation | 76.55% | 88.53% |

Values are rounded for readability.

### Goal Frequency Distribution

The observed absolute frequencies for home and away goal counts are:

| Goals Scored | Home Matches | Away Matches |
|---|---:|---:|
| 0 | 86 | 108 |
| 1 | 110 | 142 |
| 2 | 103 | 83 |
| 3 | 63 | 34 |
| 4 | 15 | 10 |
| 5 | 3 | 3 |
| **Total** | **380** | **380** |

Each frequency represents the number of matches in which the home or away team scored exactly the specified number of goals.

The distributions are analyzed independently. They do not directly represent match outcomes.

### Key Findings

**1. Higher Home Goal Production**

Across the 380 matches of the 2025/26 Premier League season, home teams scored 580 goals, compared with 465 goals scored by away teams.

This corresponds to averages of approximately 1.53 and 1.22 goals per match, respectively, indicating higher aggregate goal production by home teams.

The observed average difference is approximately 0.30 goals per match.

This finding describes the aggregate season results and does not imply that every individual team scored more goals at home.

**2. Greater Relative Variability in Away Goals**

Away goals showed a higher coefficient of variation (88.53%) than home goals (76.55%).

Although home goals had a slightly higher absolute standard deviation, away goals exhibited greater variability relative to their mean.

This distinction highlights the importance of comparing both absolute and relative measures of dispersion.

**3. More Matches Without Away Goals**

Away teams failed to score in 108 matches, compared with 86 matches in which home teams failed to score.

This difference of 22 matches indicates that scoreless performances were more frequent among away teams in the analyzed dataset.

Additionally, exactly one goal was the most frequent goal count for both home and away teams.

### Visualization Insights

The grouped bar chart reveals several descriptive patterns:

- Exactly one goal was the most frequent category for both home and away teams.
- Away teams recorded higher frequencies in the zero-goal and one-goal categories.
- Home teams recorded higher frequencies in the two-goal, three-goal, and four-goal categories.
- Both distributions recorded the same frequency for five-goal performances.
- Four-goal and five-goal performances were relatively uncommon compared with lower goal counts.

These observations describe the distribution of goals per match but do not directly establish which teams won more matches.

Match outcomes require comparing home and away goals within each individual fixture.

### Limitations

The exploratory data analysis has several limitations that should be considered when interpreting its findings.

**Single-Season Dataset**

The analysis uses match data from the 2025/26 Premier League season.

Although the dataset covers all 380 matches, the observed patterns may not generalize to other seasons.

**Limited Analytical Scope**

The current EDA focuses primarily on home and away goal distributions.

Additional match attributes and team-specific patterns have not yet been fully explored and may provide further insights.

**Descriptive, Not Causal or Predictive**

The reported statistics identify observed patterns but do not establish causal relationships.

For example, higher average home goal production does not, by itself, demonstrate that playing at home causes teams to score more goals.

No predictive model has been implemented or evaluated at this stage, so these findings do not establish predictive accuracy for future match outcomes.

**Temporal Data Leakage**

The current descriptive statistics use full-season data, which is appropriate for analyzing the completed season.

However, these aggregates cannot be directly reused as pre-match features for matches played earlier in the same season.

Future predictive development will require time-aware feature engineering, temporal validation, and safeguards against data leakage.

### Relevance to Future Predictive Modeling

The EDA provides an initial understanding of the statistical characteristics of the dataset.

Observed differences between home and away goal distributions suggest potential areas for future feature engineering and model evaluation.

However, a descriptive pattern does not guarantee predictive usefulness.

Candidate features must be evaluated using appropriate validation procedures and data that would have been available at the time of each prediction.

## Current Limitations

- The project does not yet predict match outcomes.
- Pre-match feature engineering has not yet been implemented.
- Time-aware predictive evaluation is not yet available.
- The current analysis focuses on a single Premier League season.
- EDA coverage is concentrated primarily on goal distributions.
- Automated tests cover selected calculations and data quality cases, not every possible input.
- Visualization improvements have been checked visually but are not covered by dedicated automated chart tests.
- No prediction API or deployed application is available.

## Future Development

Planned development areas include:

- Additional exploratory analysis and evaluation of existing findings.
- Applied probability, statistical inference, and econometrics.
- Data engineering, SQL, and data quality practices.
- Reproducible data processing pipelines.
- Pre-match feature engineering without temporal leakage.
- Time-aware training and validation strategies.
- Baseline prediction models and evaluation metrics.
- Machine learning models for football match outcomes.
- Model calibration and performance analysis.
- Documentation, reproducibility, and deployment practices.
- Exploratory deep learning techniques where appropriate.

These features will be developed incrementally and documented only when implemented and verified.

## Development

This project is being developed incrementally as a practical learning and portfolio project, with an emphasis on understanding the technical decisions behind each implementation.

Development follows a structured approach that combines statistical reasoning, Python programming, reusable functions, automated testing, Git version control, and technical documentation.

Each new feature is implemented, reviewed, and tested before being incorporated into the project history.

The long-term objective is to build a reliable and explainable football analytics project while developing skills in Data Science, Data Engineering, Statistics, and Machine Learning.

The project is intended to progressively evolve from descriptive football data analysis into a validated match outcome prediction system.
