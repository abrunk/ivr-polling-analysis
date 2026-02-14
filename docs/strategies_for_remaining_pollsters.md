# Strategies to Classify Remaining 10.1% of Pollsters

## Current Status
- **Classified:** 89.9% (16,702 polls from top 50 pollsters)
- **Unclassified:** 10.1% (1,879 polls from top 50 pollsters)
- **Total unknown pollsters in top 50:** 13 pollsters

## Strategy 1: Check FiveThirtyEight's Own Pollster Ratings Data

FiveThirtyEight's pollster ratings datasets might include methodology information we haven't accessed yet.

**Action:**
- Check if their pollster-ratings.csv files contain methodology columns
- Look for any metadata about pollster characteristics
- Cross-reference pollster IDs between datasets

**Files to examine:**
- `pollster-ratings/2023/pollster-ratings.csv`
- Check for any other metadata files in the pollster-ratings directories

## Strategy 2: Use Pollster Name Patterns as Heuristics

Many pollster names contain clues about their methodology:

**Likely IVR Indicators:**
- "Automated"
- "Robocall"
- Names of known IVR firms (InsiderAdvantage, Opinion Savvy)

**Likely Live Phone Indicators:**
- University names (usually have CATI centers with trained students)
- "Research Associates"
- "Opinion Research"
- Newspaper partnerships (NYT, WaPo, LA Times typically use live)

**Likely Online Indicators:**
- "Interactive"
- "Panel"
- "SurveyMonkey" (explicit)

**Action:** Create heuristic rules based on pollster name patterns

## Strategy 3: Cross-Reference with AAPOR Transparency Initiative

AAPOR maintains a transparency database of polling organizations.

**Action:**
- Search AAPOR member directory
- Check AAPOR transparency initiative disclosures
- Look for methodology statements

**URLs:**
- https://www.aapor.org/
- AAPOR transparency initiative database

## Strategy 4: Manual Web Search for Each Unknown Pollster

Systematic Google search for each of the 13 remaining pollsters.

**Search patterns:**
- "[Pollster Name] methodology"
- "[Pollster Name] IVR automated"
- "[Pollster Name] live interviewer"
- "[Pollster Name] polling methods"
- "[Pollster Name] + Wikipedia"

**Unknown pollsters to research (in priority order by poll count):**
1. Research 2000 (835 polls) - **HIGH PRIORITY**
2. TCJ Research (402 polls)
3. SurveyMonkey (217 polls)
4. Greenberg Quinlan Rosner (144 polls)
5. Mitchell Research (137 polls)
6. EPIC-MRA (132 polls)
7. RT Strategies (126 polls)
8. Los Angeles Times (118 polls)
9. Pharos Research Group (115 polls)
10. RAND Corporation (103 polls)
11. Princeton Survey Research Associates (102 polls)
12. Angus Reid Global (99 polls)
13. George Washington University (95 polls)
14. ccAdvertising (89 polls)

## Strategy 5: Check Academic Papers on Polling Methodology

Search for academic papers that discuss polling methodologies in the 2012-2018 period.

**Search terms:**
- "polling methodology 2012 election IVR"
- "robopolls accuracy 2016 election"
- "survey mode effects presidential polling"

**Databases:**
- Google Scholar
- JSTOR
- Political Science research databases

**Papers might include tables classifying pollsters by methodology**

## Strategy 6: Check Historical News Coverage

News articles about polling often mention methodology.

**Search patterns:**
- "[Pollster Name] criticized for methodology"
- "[Pollster Name] accuracy 2012"
- "[Pollster Name] uses robocalls"
- Site-specific searches: site:fivethirtyeight.com "[Pollster Name]"

## Strategy 7: Examine Poll Comments in Our Data

The FiveThirtyEight data includes a "comment" column that sometimes mentions methodology.

**Action:**
- Extract and examine all comments for unknown pollsters
- Look for methodology mentions
- Check for notes like "previously listed as [methodology]"

## Strategy 8: Contact Information from Known Defunct Pollsters

Some pollsters may be defunct, making research harder.

**Action:**
- Identify likely defunct pollsters (e.g., Research 2000 was discredited)
- Search for archival information
- Check Wayback Machine for their old websites
- Look for news about their closure/scandal

## Strategy 9: Use Pollster Partisan Affiliation as Proxy

Internal pollsters (D) or (R) often use live phone for quality.

**Heuristic:**
- Partisan internal pollsters → Likely Live Phone
- Non-partisan budget pollsters → Could be IVR or Online

**Limitations:** This is a weak signal, use only as last resort

## Strategy 10: Fuzzy Matching Improvements

Our current fuzzy matching might miss some matches.

**Action:**
- Improve fuzzy matching algorithm
- Handle common name variations:
  - "Public Policy Polling" vs "PPP"
  - "Rasmussen Reports" vs "Rasmussen" vs "Scott Rasmussen"
  - University name variations
- Create alias mapping for known variants

## Strategy 11: Check Original 2010 Thesis Documentation

Your thesis might have notes about pollsters beyond the data file.

**Action:**
- Review thesis methodology chapter
- Check for pollster classification tables
- Look for footnotes about methodology

## Strategy 12: Time-Based Heuristics

Methodology usage changed over time.

**Heuristic:**
- Pre-2014: More likely IVR (peak IVR era)
- Post-2016: More likely Online/Mixed (cell phone problems for IVR)

**Action:**
- Analyze when each unknown pollster was most active
- Apply temporal heuristics carefully

## Recommended Workflow

**Phase 1: Quick Wins (30 min)**
1. Check FiveThirtyEight pollster-ratings files for methodology data
2. Extract and review "comment" column from our data
3. Apply name-based heuristics for obvious cases

**Phase 2: Targeted Research (1-2 hrs)**
4. Web search top 5 unknown pollsters (Research 2000, TCJ, etc.)
5. Check AAPOR transparency database
6. Improve fuzzy matching for common name variants

**Phase 3: Deep Dive (if needed)**
7. Academic paper search
8. Historical news search
9. Wayback Machine for defunct pollsters

**Phase 4: Final Classifications**
10. Apply informed heuristics for remaining cases
11. Document confidence levels (high/medium/low)
12. Accept that some may remain unknown

## Expected Outcomes

**Optimistic:** 95-98% coverage (classify 8-10 more pollsters)
**Realistic:** 92-95% coverage (classify 5-8 more pollsters)
**Pessimistic:** 90-92% coverage (classify 2-4 more pollsters)

**Diminishing returns:** The last few pollsters may be defunct, poorly documented, or genuinely mixed methodology

## Priority Targets

Focus on these for maximum impact:

1. **Research 2000** (835 polls) - MUST investigate, huge impact
2. **TCJ Research** (402 polls) - Significant volume
3. **SurveyMonkey** (217 polls) - Well-known, should be findable
4. **Greenberg Quinlan Rosner** (144 polls) - Major Democratic firm
5. **Los Angeles Times** (118 polls) - Major newspaper

These 5 alone represent 1,816 polls (74% of unknown)
