# IVR Polling Analysis (2006-2018)

A modern reanalysis of Interactive Voice Response (IVR) polling accuracy across multiple U.S. election cycles, examining how automated polling methods compared to traditional live interviewer surveys.

## Project Overview

This project extends and modernizes my 2014 master's thesis research on IVR polling by:
- Expanding the analysis from a single election cycle (2010) to seven cycles (2006-2018)
- Applying contemporary statistical and machine learning methods
- Creating reproducible, publication-quality visualizations
- Examining how IVR polling performance evolved as cell phone adoption increased

## Research Questions

1. How do IVR polls compare to live interviewer polls in measuring undecided voters?
2. Did IVR polling accuracy change over time (2006-2018) as cell phone penetration increased?
3. Which factors (pollster characteristics, timing, sample size, state) best predict polling accuracy?
4. Can machine learning methods improve upon traditional regression approaches for understanding polling performance?

## Data Sources

### Polling Data
- **2006-2012**: HuffPost Pollster API (successor to Pollster.com)
- **2014-2018**: FiveThirtyEight pollster ratings dataset

### Election Results
- **2006-2018**: FiveThirtyEight election results repository

### Focus
- Gubernatorial general elections
- U.S. Senate general elections
- Survey methodology comparisons: IVR vs. Live Phone vs. Online

## Methodology

### Statistical Approaches
- **Traditional**: Linear regression, mixed-effects models accounting for state/pollster clustering
- **Machine Learning**: Random forests, gradient boosting for prediction and feature importance
- **Model Comparison**: Cross-validation, performance metrics across approaches

### Key Variables
- **Dependent Variables**: Undecided voter percentage, polling error, bias
- **Independent Variables**: Survey mode (IVR/Live/Online), days before election, sample size, pollster characteristics, state, year
- **Controls**: Election competitiveness, partisan lean, turnout model (LV/RV/A)

## Project Structure

```
ivr-polling-analysis/
├── data/
│   ├── raw/              # Original data from sources
│   │   ├── fivethirtyeight/
│   │   ├── huffpost/
│   │   └── election-results/
│   └── processed/        # Cleaned, combined datasets
├── R/                    # Analysis scripts
│   ├── 01-data-collection.R
│   ├── 02-data-cleaning.R
│   ├── 03-eda.R
│   ├── 04-traditional-models.R
│   ├── 05-ml-models.R
│   └── 06-visualization.R
├── analysis/             # Analysis outputs (markdown)
├── figures/              # Publication-quality plots
└── docs/                 # Documentation

```

## Requirements

- R (>= 4.0)
- tidyverse
- tidymodels
- ggplot2
- Other packages listed in `renv.lock`

## Author

Alexander Brunk
GitHub: [@abrunk](https://github.com/abrunk)

## License

MIT

## Acknowledgments

This project builds on my 2014 master's thesis research at [University]. Original 2010 data collection involved manual scraping of Pollster.com polling data.
