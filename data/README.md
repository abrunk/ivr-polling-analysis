# Data Sources and Documentation

## Overview

This directory contains polling and election results data for U.S. gubernatorial and Senate races from 2006-2018.

## Data Sources

### 1. FiveThirtyEight Pollster Ratings (2014-2018)

**Source:** [FiveThirtyEight GitHub - pollster-ratings](https://github.com/fivethirtyeight/data/tree/master/pollster-ratings)

**Files:**
- `raw/fivethirtyeight/raw-polls-2014.tsv` (6,614 polls)
- `raw/fivethirtyeight/raw-polls-2016.csv` (7,977 polls)
- `raw/fivethirtyeight/raw-polls-2018.csv` (8,512 polls)

**Format Note:** 2014 uses TSV format; 2016 and 2018 use CSV format

**Key Variables:**
- `methodology`: Survey mode (Live Phone, IVR, Online, Mail, etc.)
- `pollster`: Polling organization name
- `samplesize`: Number of respondents
- `polldate`: Date of poll
- `electiondate`: Date of election
- `type_simple`: Race type (Sen, Gov, Pres, House)
- `location`: State
- `cand1_pct`, `cand2_pct`: Candidate vote percentages
- `error`: Polling error (poll margin - actual margin)
- `bias`: Directional bias
- And many more...

### 2. HuffPost Pollster API (2006-2012)

**Source:** [HuffPost Pollster API](http://elections.huffingtonpost.com/pollster/api/v2)

**Status:** Script created (`R/01-data-collection-huffpost.R`) - requires manual testing and execution

**Note:** HuffPost Pollster is the successor to Pollster.com (original source for 2010 thesis data)

**Target Files:**
- `raw/huffpost/polls_2006_senate.csv`
- `raw/huffpost/polls_2006_governor.csv`
- `raw/huffpost/polls_2008_senate.csv`
- `raw/huffpost/polls_2008_governor.csv`
- `raw/huffpost/polls_2010_senate.csv`
- `raw/huffpost/polls_2010_governor.csv`
- `raw/huffpost/polls_2012_senate.csv`
- `raw/huffpost/polls_2012_governor.csv`

### 3. Election Results

**Source:** [FiveThirtyEight election-results](https://github.com/fivethirtyeight/election-results)

**Files:**
- `raw/election-results/election_results_senate.csv` (4,133 records from 1998-present)
- `raw/election-results/election_results_gubernatorial.csv` (2,352 records from 1998-present)

**Key Variables:**
- `cycle`: Election year
- `state`, `state_abbrev`: State information
- `stage`: primary/general/runoff
- `special`: TRUE/FALSE
- `candidate_name`: Candidate
- `party`: Political party
- `votes`, `percent`: Vote totals and percentages
- `winner`: TRUE/FALSE

## Data Harmonization Strategy

Since data comes from two different sources (HuffPost 2006-2012, FiveThirtyEight 2014-2018), we need to harmonize variables:

### Variable Mapping

| Variable Purpose | HuffPost Name | FiveThirtyEight Name | Notes |
|---|---|---|---|
| Survey methodology | TBD | `methodology` | Need to verify HuffPost API structure |
| Poll date | TBD | `polldate` | May need date parsing |
| Election date | TBD | `electiondate` | |
| Sample size | TBD | `samplesize` | |
| Pollster | TBD | `pollster` | May need standardization |
| State | TBD | `location` | |
| Race type | TBD | `type_simple` | Gov/Sen |
| Undecided % | TBD | Calculated | May need to derive |

### Data Quality Checks

When combining data sources, verify:
1. Consistent methodology coding (IVR vs "Automated" vs "Robocall")
2. Date formats match
3. No duplicate polls across sources
4. Undecided voters calculated consistently
5. Sample type (LV/RV/A) coded uniformly

## Directory Structure

```
data/
├── raw/                          # Original data from sources
│   ├── fivethirtyeight/         # 2014-2018 polls
│   ├── huffpost/                # 2006-2012 polls (to be collected)
│   └── election-results/        # Actual election outcomes
├── processed/                    # Cleaned, combined datasets
│   ├── polls_combined_2006-2018.csv
│   ├── polls_with_results.csv
│   └── polls_undecideds.csv
└── README.md                     # This file
```

## Next Steps

1. ✅ Download FiveThirtyEight polling data (2014, 2016, 2018)
2. ✅ Download FiveThirtyEight election results
3. ⏳ Test and execute HuffPost Pollster API data collection
4. ⏳ Explore and document HuffPost API data structure
5. ⏳ Create data harmonization/cleaning scripts
6. ⏳ Combine all polling data into unified dataset
7. ⏳ Merge with election results for accuracy calculations
8. ⏳ Calculate undecided voter percentages
9. ⏳ Generate data quality report

## Data Citations

### FiveThirtyEight
- Pollster Ratings: Available at https://github.com/fivethirtyeight/data/tree/master/pollster-ratings
- Election Results: Available at https://github.com/fivethirtyeight/election-results

### HuffPost Pollster
- API Documentation: https://app.swaggerhub.com/api/huffpostdata/pollster-api/
- Original Pollster.com data now maintained by HuffPost

## Contact

For questions about data sources or methodology, contact Alexander Brunk.
