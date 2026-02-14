# Data Collection Status Summary

## Data Successfully Collected

### FiveThirtyEight Pollster Ratings (2014, 2016, 2018)
✅ **Status:** Downloaded and verified

- `raw-polls-2014.tsv` - 6,614 polls
- `raw-polls-2016.csv` - 7,977 polls
- `raw-polls-2018.csv` - 8,512 polls

**Issue:** These files do NOT contain methodology information (IVR vs Live Phone)

### FiveThirtyEight State of the Polls (2012)
✅ **Status:** Downloaded and verified

- `2012_polls.csv` - 1,838 polls
- `2012_races.csv` - 468 races

**Issue:** This file also lacks methodology column

### Election Results
✅ **Status:** Downloaded and verified

- `election_results_senate.csv` - 4,133 results (1998-present)
- `election_results_gubernatorial.csv` - 2,352 results (1998-present)

## The Methodology Problem

**None of the FiveThirtyEight datasets we've downloaded contain survey methodology information** (IVR vs Live Phone vs Online, etc.).

This is a critical variable for our analysis since the whole point is to compare IVR polling to traditional live interviewer methods.

## Solutions

### Option 1: Manual Pollster Classification (RECOMMENDED for MVP)

Create a manual mapping of major pollsters to their methodologies based on:

**Known IVR Pollsters (2012-2018):**
- Rasmussen Reports - IVR
- Public Policy Polling (PPP) - IVR
- SurveyUSA - IVR
- YouGov - Online (not IVR, but automated)

**Known Live Phone Pollsters:**
- Gallup - Live Phone
- Pew Research - Live Phone
- ABC News/Washington Post - Live Phone
- CBS News/New York Times - Live Phone
- NBC News/Wall Street Journal - Live Phone
- Quinnipiac - Live Phone
- Marist - Live Phone

**Sources for classification:**
- Research papers on polling methodology
- Pollster websites/methodology pages
- AAPOR (American Association for Public Opinion Research) pollster directories
- FiveThirtyEight's written articles about pollster methodologies

**Pros:**
- Can start analysis immediately with known major pollsters
- Covers majority of poll volume (major pollsters conduct most polls)
- Highly accurate for classified pollsters

**Cons:**
- Won't capture every poll (some pollsters unknown/mixed methodology)
- Manual work required
- May miss smaller pollsters

### Option 2: Use FiveThirtyEight's IVR-specific pollster ratings page

FiveThirtyEight has a page specifically for IVR pollsters at:
https://projects.fivethirtyeight.com/pollster-ratings/ivr-polls/

This could provide a list of IVR pollsters to cross-reference.

### Option 3: Focus on 2014-2018 with pollster subset

If we can't get comprehensive methodology data for 2012, we could:
- Use 2014, 2016, 2018 data only (still 3 cycles, 23k polls)
- Focus on analyzing only well-documented major pollsters
- Still a publishable analysis with strong N

### Option 4: Contact researchers / Use Roper iPoll

- Roper iPoll archive (requires institutional access) has detailed methodology
- Could contact polling methodology researchers who may have this data
- Time-intensive but most comprehensive

## Recommendation

**Phase 1:** Create manual pollster-methodology mapping for top 30-50 pollsters
- These likely represent 70-80%+ of total poll volume
- Can validate against multiple sources
- Allows us to start analysis quickly

**Phase 2:** Supplement with web research for remaining pollsters as needed
- Add pollsters incrementally as we encounter them in analysis
- Document sources for each classification

**Phase 3:** Sensitivity analysis
- Compare results using "known pollsters only" vs. "all polls"
- Report which polls were excluded due to unknown methodology

## Next Steps

1. Extract list of pollsters from our 2012-2018 data, ranked by frequency
2. Research and classify top 50 pollsters by methodology
3. Create `pollster_methodology_mapping.csv` reference file
4. Begin data cleaning and merging with methodology assignments
5. Document classification sources and any ambiguous cases

## Data Quality Notes

- All FiveThirtyEight data includes pollster names, dates, sample sizes
- Election results data is complete and well-structured
- Main gap is methodology classification, which is solvable through research
