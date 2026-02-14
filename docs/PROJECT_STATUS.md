# IVR Polling Analysis - Project Status

**Last Updated:** February 14, 2026

## ✅ Completed

### Data Collection
- **2012-2018 Polling Data:** 24,941 polls from FiveThirtyEight
  - 2012: 1,838 polls
  - 2014: 6,614 polls
  - 2016: 7,977 polls
  - 2018: 8,512 polls
- **Election Results:** Complete Senate and Gubernatorial results (1998-present)
- **Pollster Methodology Mapping:** 119 pollsters from 2010 thesis data
  - 20 IVR pollsters
  - 95 Live Phone pollsters
  - 4 Internet pollsters

### Analysis Tools
- Python scripts for pollster coverage analysis
- Methodology extraction from thesis data
- Coverage analysis shows 62.4% of top 50 pollster polls are matched

### Known IVR Pollsters (High Confidence)
- SurveyUSA (2,309 polls)
- Rasmussen Reports/Pulse Opinion Research (1,991 polls)
- Scott Rasmussen (271 polls)
- We Ask America (185 polls)
- InsiderAdvantage (93 polls)
- Public Policy Polling (1,237 polls - **needs verification**)

### Known Live Phone Pollsters (High Confidence)
- Mason-Dixon (1,242 polls combined)
- Quinnipiac University (538 polls)
- Marist College (433 polls)
- Suffolk University (203 polls)
- CBS News/New York Times (162 polls)
- ABC News/Washington Post (161 polls)
- Siena College (150 polls)
- Ipsos (174 polls)
- Dan Jones & Associates (99 polls)
- Global Strategy Group (84 polls)

## 🚧 In Progress / Next Steps

### Immediate Priority: Expand Methodology Mapping
**Goal:** Map remaining pollsters to achieve 80%+ coverage

**Unmatched Major Pollsters to Research:**
1. **Public Policy Polling** (1,237 polls) - Known IVR but using different name format
2. **Gallup** (407 polls) - Live Phone
3. **American Research Group** (768 polls) - Needs verification
4. **Research 2000** (835 polls) - Needs verification
5. **University of New Hampshire** (279 polls) - Likely Live
6. **Harris Interactive** (270 polls) - Online
7. **CNN/Opinion Research** (259 polls) - Live Phone
8. **Monmouth University** (197 polls) - Live Phone
9. **Emerson College** (121 polls) - Online/IVR mix

**Sources for Classification:**
- AAPOR pollster directory
- FiveThirtyEight pollster ratings: https://projects.fivethirtyeight.com/pollster-ratings/ivr-polls/
- Individual pollster methodology pages
- Academic papers on 2012-2018 polling methods

### Data Cleaning & Harmonization
1. Standardize pollster names across datasets
2. Filter for gubernatorial and Senate races only
3. Merge with election results
4. Calculate undecided voter percentages
5. Create unified dataset with methodology flags

### Analysis Development
1. Exploratory data analysis (EDA)
2. Replicate 2010 thesis analysis on 2012-2018 data
3. Time series analysis of IVR vs Live Phone accuracy
4. Mixed-effects models accounting for state/pollster clustering
5. Machine learning models for comparison

## 📊 Data Summary

**Total Coverage:**
- 4 consecutive election cycles (2012, 2014, 2016, 2018)
- 562 unique pollsters
- ~25,000 polls
- Methodology known for ~60-65% of polls (expandable to 80%+)

**Race Types:**
- Presidential
- Senate
- House
- Gubernatorial
- Generic Ballot

**For Our Analysis Focus:**
- Filter to gubernatorial + Senate races only
- Exclude special elections (optional)
- Focus on general elections (not primaries)

## 🎯 Research Questions

1. How do IVR polls compare to live interviewer polls in measuring undecided voters?
2. Did IVR polling accuracy change 2012-2018 as cell phone penetration increased?
3. Which pollster characteristics best predict accuracy?
4. Can ML methods improve upon traditional regression for understanding polling performance?

## 📁 Repository Structure

```
ivr-polling-analysis/
├── data/
│   ├── raw/
│   │   ├── fivethirtyeight/     (~25k polls, 2012-2018)
│   │   └── election-results/    (~6k results, 1998-present)
│   └── processed/
│       └── pollster_methodology_2010.csv  (119 pollsters)
├── R/
│   ├── extract_thesis_methodology.py
│   └── analyze_pollster_coverage.py
├── docs/
│   ├── data-status-summary.md
│   └── PROJECT_STATUS.md (this file)
├── analysis/    (empty - future markdown reports)
├── figures/     (empty - future visualizations)
└── README.md
```

## 💡 Key Insights So Far

1. **HuffPost Pollster API is defunct** - Had to pivot to FiveThirtyEight data for all years
2. **FiveThirtyEight data lacks methodology columns** - Required creative solution using thesis data
3. **Thesis data is gold** - Provides validated pollster-methodology mapping for 2010 that largely carries forward
4. **Coverage is good** - Top 50 pollsters cover 75% of all polls; matching 62% is strong foundation
5. **Clean data structure** - FiveThirtyEight data is well-formatted and consistent

## 🔄 Git History

- `4584417` - Initial project setup
- `1f7227d` - Add 2012 data and methodology mapping

## 📧 Contact

Alexander Brunk (@abrunk)
