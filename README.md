# Examining the Relationship Between Polling Methodology and Undecided Voters

**Master's Thesis (2011)**
**Author:** Alexander Brunk
**GitHub:** [@abrunk](https://github.com/abrunk)

---

## Introduction

This repository presents a modern reanalysis of my 2011 master's thesis examining how Interactive Voice Response (IVR) polling and live phone interviewing differ in their measurement of undecided voters. The original thesis analyzed 805 polls from the 2010 U.S. Senate and Gubernatorial elections and found that IVR polls consistently showed fewer undecided voters than live phone polls—a statistically significant difference with important implications for polling aggregation and interpretation.

**Original thesis repository:** [thesis_ivr_polling](https://github.com/abrunk/thesis_ivr_polling)

### Why Revisit This Research?

Fifteen years after the original analysis, modern data science tools and expanded data availability enable us to:

1. **Apply contemporary visualization techniques**: Using seaborn and matplotlib to create publication-quality figures that better communicate the findings
2. **Leverage improved statistical methods**: Robust standard errors (HC3), better model diagnostics, and more transparent reproducible workflows
3. **Access comprehensive polling archives**: FiveThirtyEight and other sources now provide systematic polling data across multiple election cycles (2008-2016)
4. **Examine temporal evolution**: Test whether the original finding held as the polling landscape changed dramatically due to cell phone adoption
5. **Investigate new questions**: The extended analysis discovered systematic partisan bias in IVR polls—something the original thesis did not examine

This repository documents both the **original 2010 thesis findings** with modern visualizations and serves as the foundation for **extended analyses** examining IVR polling performance across presidential, Senate, and gubernatorial races from 2008-2016.

---

## Abstract

This thesis investigates whether Interactive Voice Response (IVR) polling and traditional live phone interviewing produce different estimates of undecided voters in U.S. elections. Analyzing 805 polls from the 2010 Senate and Gubernatorial races, I find that **IVR polls show significantly fewer undecided voters** than live phone polls (8.2% vs 10.5%, difference: -2.3pp, p<0.001). This finding has important implications for understanding polling methodology bias and the interpretation of pre-election surveys.

---

## Literature Review and Theoretical Framework

### The Rise of IVR Polling

Interactive Voice Response (IVR) polling emerged in the late 1990s and early 2000s as a cost-effective alternative to traditional live interviewer surveys. By 2010, IVR polls constituted a substantial portion of public polling, particularly from firms like SurveyUSA, Rasmussen Reports, and Public Policy Polling (PPP). The methodology uses automated phone systems that ask pre-recorded questions and collect responses via touch-tone keypresses.

**Key differences from live phone interviewing:**
- **Cost**: IVR polls cost 30-50% less than live interviewer surveys (Keeter 2007)
- **Speed**: Can field large samples in 24-48 hours vs. 5-7 days for live phone
- **Standardization**: Eliminates interviewer effects and question wording variation
- **Coverage**: Limited to landlines in 2010 due to Telephone Consumer Protection Act (TCPA) restrictions on automated calls to cell phones

### Mode Effects in Survey Research

Survey methodologists have long documented that how a question is asked affects how it is answered. The literature on mode effects identifies several mechanisms:

**1. Social Desirability Bias (Tourangeau & Smith 1996)**
- Respondents give socially acceptable answers when speaking to a human interviewer
- More pronounced for sensitive questions (vote choice, approval ratings)
- Automated systems reduce social pressure, potentially yielding more honest responses

**2. Satisficing (Krosnick 1991)**
- Respondents sometimes give "good enough" answers rather than optimal ones
- Live interviewers can probe hesitation or non-responses
- IVR requires explicit action to select "don't know" or "undecided"

**3. Response Effects (Holbrook et al. 2003)**
- Question order, interviewer characteristics, and perceived anonymity all influence responses
- IVR offers complete anonymity; live phone provides perceived human connection
- Different respondent motivations may yield different substantive answers

### Undecided Voters in Pre-Election Polls

The proportion of undecided voters serves as a crucial indicator of election uncertainty and poll reliability:

**Why undecided rates matter:**
- **Poll aggregation**: Mixing polls with different undecided rates introduces error
- **Margin of error**: Traditional MOE calculations assume all voters have preferences
- **Late deciders**: Higher undecided rates signal potential volatility
- **Pollster allocations**: How pollsters allocate undecideds affects final estimates

**Prior findings:**
- Undecided rates decline non-linearly as Election Day approaches (Gelman & King 1993)
- Pollsters using different methodologies report different undecided rates, but the causes are unclear
- No consensus on whether IVR or live phone better captures "true" uncertainty

### Research Gap

Despite extensive research on mode effects in surveys, no study had systematically compared IVR and live phone polls specifically on undecided voter measurement. This thesis addresses that gap by:

1. Analyzing a large sample (805 polls) from a single election cycle (2010)
2. Controlling for temporal effects, sample size, and race characteristics
3. Using robust regression methods to isolate the methodology effect
4. Testing whether the effect varies over the campaign (interaction with timing)

---

## Research Question

**Do IVR (automated phone) polls and live interviewer polls produce different estimates of undecided voters?**

### Hypothesis

IVR polls will show **fewer** undecided voters than live phone polls because:

1. **Social desirability bias reduction**: Respondents may be more comfortable admitting uncertainty to an automated system than to a human interviewer
2. **Measurement differences**: IVR requires explicit keypress responses, potentially discouraging non-committal "don't know" answers
3. **Response pressure**: Automated systems may create less social pressure to have a formed opinion

---

## Main Finding

![Main Finding](figures/thesis_fig1_main_finding.png)

**IVR polls showed 2.3 percentage points fewer undecided voters than live phone polls (p<0.001)**

| Methodology | Mean Undecided | Std. Dev. | N |
|-------------|---------------|-----------|---|
| **Live Phone** | **10.5%** | 7.3% | 270 |
| **IVR** | **8.2%** | 5.6% | 535 |
| **Difference** | **-2.3pp** | | |

- **t-statistic**: -5.04
- **p-value**: <0.001 (highly significant)
- **Effect size**: Cohen's d = 0.35 (small to medium)

---

## Data and Methodology

### Data Collection

**Sample:** 805 polls from 2010 U.S. Senate and Gubernatorial general elections

**Sources:**
- RealClearPolitics polling aggregator
- Pollster.com (now HuffPost Pollster)
- Individual pollster websites

**Inclusion criteria:**
- Polls conducted within 90 days of Election Day
- Clear methodology designation (IVR or Live Phone)
- Reported undecided/don't know percentage
- Minimum sample size of 300 likely/registered voters

### Variables

**Dependent Variable:**
- Undecided voter percentage (calculated as 100 - Democrat% - Republican% - Other%)

**Independent Variables:**
- Survey methodology (IVR vs Live Phone)
- Days until election
- Sample size
- State
- Poll sponsorship type

### Statistical Analysis

**Weighted Least Squares Regression** with quadratic temporal controls:

```
Undecided = β₀ + β₁(IVR) + β₂(Days) + β₃(Days²) + β₄(IVR × Days) + ε
```

- **Weighting**: Polls weighted by 2√N (sample size)
- **Robust standard errors**: HC3 heteroskedasticity-consistent estimator
- **Model fit**: R² = 0.307

---

## Results

### Distribution Comparison

![Distributions](figures/thesis_fig2_distributions.png)

The distributions show that:
- IVR polls are more tightly clustered around lower undecided rates
- Live phone polls show greater variability
- The difference is consistent across the distribution, not driven by outliers

### Temporal Dynamics

![Temporal](figures/thesis_fig3_temporal.png)

Undecided voters decline as Election Day approaches in **both** methodologies:
- Both show classic campaign convergence pattern
- IVR consistently shows fewer undecideds throughout the campaign
- The gap remains stable over time (no significant interaction effect)

### Regression Model Results

![Model Results](figures/thesis_fig4_model_results.png)

**Key findings from the regression model:**

| Variable | Coefficient | Std. Error | p-value | Significance |
|----------|------------|------------|---------|--------------|
| **IVR Effect** | **-3.55pp** | 0.53 | <0.001 | *** |
| Days (Linear) | 0.43 | 0.04 | <0.001 | *** |
| Days² (Quadratic) | -0.002 | 0.0003 | <0.001 | *** |
| IVR × Days | -0.01 | 0.05 | 0.89 | n.s. |

**Interpretation:**
- IVR methodology reduces undecided percentage by 3.6pp after controlling for campaign timing
- Undecided voters decline non-linearly as Election Day approaches (quadratic term significant)
- No evidence that IVR's effect changes over the campaign (interaction not significant)

---

## Discussion

### Summary of Findings

The analysis of 805 polls from the 2010 Senate and Gubernatorial races reveals a **robust and statistically significant difference** in how IVR and live phone polls measure undecided voters:

- **Simple comparison**: IVR polls showed 2.3 percentage points fewer undecided voters (8.2% vs 10.5%)
- **Regression-adjusted estimate**: 3.6 percentage points fewer after controlling for campaign timing, sample size, and state
- **Statistical significance**: p < 0.001 across all specifications
- **Effect persistence**: The difference remained constant throughout the campaign period (no interaction effect)

This finding suggests that survey methodology systematically affects a substantively important survey measure—one that influences both poll interpretation and aggregation methods.

### Why Does IVR Show Fewer Undecideds?

Three theoretical mechanisms could explain this pattern:

**1. Social Desirability and Response Effects**

The most theoretically compelling explanation involves differential social pressure:

- **Anonymity hypothesis**: Respondents speaking to a recorded message may feel less pressure to appear informed than when speaking to a human interviewer. Admitting uncertainty to a machine carries no social cost.
- **Interviewer effects**: Live interviewers can probe hesitation ("Are you leaning toward either candidate?"), potentially converting soft undecideds into expressed preferences. IVR systems accept the first response.
- **Satisficing differences**: The cognitive effort required to press "9" for undecided in IVR may be similar to the effort of expressing a preference, whereas live interviews create an asymmetry where expressing uncertainty is easier.

**Empirical support:** The effect size (3.6pp) aligns with social desirability effects found in other survey contexts (Tourangeau & Smith 1996).

**2. Measurement Artifact**

Methodological differences in how responses are captured could create artificial differences:

- **Coding thresholds**: Live interviewers must subjectively code hesitation, silence, or qualified responses ("I'm not sure... maybe Smith?"). IVR requires explicit keypress selection.
- **Question timing**: IVR systems may play the full question before accepting responses; live interviewers sometimes record answers before finishing the question.
- **Response options**: The order and emphasis of "undecided" in the response options may differ between modes.

**Evidence against:** If this were purely a measurement artifact, we would expect greater variability in the IVR effect across pollsters, but the effect is remarkably consistent (visible in Figure 1's tight IVR distribution).

**3. Sample Composition (Differential Selection)**

IVR and live phone may reach systematically different populations:

- **Selection into response**: People who complete IVR surveys may differ from live phone respondents in political engagement or certainty.
- **Contact rates**: IVR and live phone may have different success rates with different demographic groups.
- **Callback protocols**: Live phone surveys typically use more aggressive callback schedules, potentially reaching less-engaged voters.

**Evidence against:** In 2010, both methodologies were landline-only, limiting the scope for coverage differences. This mechanism becomes more important in later years (2012+) when cell phone coverage issues emerged.

### The Most Likely Explanation

The evidence points toward a **combination of social desirability reduction and measurement standardization**. IVR's anonymity allows respondents to more comfortably express uncertainty, while its standardized measurement protocol prevents interviewers from converting soft undecideds into candidate preferences through probing.

Importantly, this finding does NOT tell us which methodology is "correct"—we cannot validate against true voter uncertainty. Instead, it reveals that **methodology choice affects the measurement**, which has practical implications for poll consumers and aggregators.

**Historical context:** This thesis predates the cell phone coverage crisis. In 2010, landline coverage was still ~73% of U.S. households, meaning both IVR and live phone had similar coverage (though both excluded the ~27% cell-only households). The extended analysis (2008-2016) shows that coverage problems dramatically worsened the situation, particularly for IVR which remained landline-only while live phone surveys could legally call cell phones.

### Implications for Poll Consumers

**1. Aggregation introduces systematic error**

Poll aggregators like RealClearPolitics and FiveThirtyEight mix IVR and live phone polls, often without methodology adjustments. If IVR polls systematically underestimate undecided voters by 2-4 percentage points, aggregated averages are biased toward whichever methodology dominates the sample.

*Example:* In a competitive race with genuine uncertainty, an average showing 6% undecided might actually represent 8-9% if the average over-weights IVR polls. This affects interpretations of race volatility and the potential for late-breaking movement.

**2. Comparability across time requires methodology consistency**

Comparing "undecided voter trends" over time is only meaningful if methodology composition remains constant. A decline in undecided voters from 12% to 8% could reflect:
- Genuine opinion crystallization (what analysts assume)
- A shift from live phone to IVR dominance in the polling sample (methodological artifact)

**3. Margin of error calculations assume full preference expression**

Traditional MOE calculations assume all respondents have preferences. Higher true undecided rates mean the effective margin of error is larger than reported. If IVR underestimates undecideds, analysts may be overconfident in IVR-based conclusions.

### Implications for Pollsters

**1. Methodology choice is not neutral**

Pollsters selecting IVR for cost reasons should recognize they are making a substantive choice that affects their findings. The 3.6pp effect is meaningful—larger than many pollsters' stated margin of error.

**2. House effects may partially reflect methodology**

Pollster "house effects" (systematic differences from the average) may not solely reflect weighting choices or likely voter models. Methodology-driven differences in undecided measurement can cascade through allocation decisions and topline results.

**3. Transparency requirements**

Given these systematic differences, pollsters should:
- Report methodology prominently (many hide it in fine print)
- Disclose how undecided voters are allocated to candidates (if at all)
- Consider methodology-adjusted aggregation in multi-mode polling firms

### Implications for the Extended Analysis

This thesis finding motivated several follow-up research questions addressed in the extended analysis:

1. **Partisan bias**: If IVR and live phone measure undecided voters differently, do they also measure *partisan* preferences differently? (Answer: Yes—IVR shows systematic pro-Republican bias)

2. **Temporal evolution**: Did the undecided rate difference persist as cell phone adoption grew? (Answer: Yes, and coverage problems compounded the bias)

3. **Race type consistency**: Does the finding hold for presidential races, not just Senate/Governor? (Answer: Yes, robust across race types)

4. **Practical significance**: Which methodology is more accurate? (Answer: Complex—IVR's coverage problems worsened over time, overwhelming any measurement advantages)

---

## Limitations

1. **Observational design**: Cannot definitively establish causal mechanism
2. **Limited to 2010**: Single election cycle; patterns may vary over time
3. **Unmeasured confounds**: Pollster quality, question wording, sample frame differences
4. **No validation against actual behavior**: Cannot determine which methodology is "correct"
5. **Pre-cell phone crisis**: Analysis predates major landline coverage problems (2012+)

---

## Files in This Repository

### Original Thesis (2010)

**Visualizations:**
- `figures/thesis_fig1_main_finding.png` - Main results (violin plot with individual polls)
- `figures/thesis_fig2_distributions.png` - Distribution comparison (histogram + box plot)
- `figures/thesis_fig3_temporal.png` - Temporal dynamics with LOWESS smoothing
- `figures/thesis_fig4_model_results.png` - Regression coefficient plot with 95% CIs

**Code:**
- `R/create_thesis_visualizations.py` - Generates all thesis figures using seaborn/matplotlib
  - Reads data from original thesis repository
  - Creates publication-quality figures with 300 DPI resolution
  - Applies HC3 robust standard errors to regression models
  - Implements LOWESS smoothing for temporal trends

**Data:**
- Original thesis data available at: [thesis_ivr_polling](https://github.com/abrunk/thesis_ivr_polling)
  - `Data/2010 Undecideds Data - Cleaned CSV.csv` (805 polls)

### Extended Analysis (2008-2016)

**Data:**
- `data/raw/fivethirtyeight/` - FiveThirtyEight polling archive
- `data/processed/` - Cleaned and merged datasets

**Analysis Scripts:**
- `R/presidential_primary_quadratic.py` - 2016 primary analysis (Trump effect)
- `R/general_election_analysis.py` - Presidential general elections (partisan bias)
- `R/senate_governor_analysis.py` - Down-ballot races (2008-2016)
- `R/thesis_2010_partisan_bias.py` - Reanalysis of 2010 data for partisan bias
- `R/comprehensive_partisan_bias_summary.py` - Synthesis across all race types
- `R/create_readme_figures.py` - Extended analysis visualizations

**Results:**
- `results/` - Regression outputs, summary statistics, bias estimates
- `figures/` - Extended analysis visualizations

---

## Reproducibility

### Requirements
```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels
```

### Generate Figures
```bash
python create_thesis_visualizations.py
```

All figures will be saved to `figures/` directory.

---

## Extended Analysis: IVR Polling Bias (2008-2016)

The original thesis focused on undecided voter measurement in a single election cycle (2010). Fifteen years later, with access to comprehensive polling archives from FiveThirtyEight and improved analytical methods, I extended the analysis to examine:

### Key Research Questions

1. **Does the undecided rate finding generalize?** Test whether IVR polls consistently show fewer undecided voters across presidential, Senate, and gubernatorial races (2008-2016)

2. **Is there partisan bias?** The original thesis did not examine whether IVR systematically favors one party. Does IVR polling show pro-Republican or pro-Democratic bias?

3. **How did coverage problems affect results?** Cell-only households grew from 20% (2008) to 51% (2016). IVR remained landline-only while live phone could call cell phones. What impact did this have?

4. **Primary vs. general elections:** Does IVR perform differently in primaries? Was there a "Trump effect" in 2016?

### Major Findings from Extended Analysis

**1. Systematic Pro-Republican Bias (2008-2016)**
- **Republicans**: IVR polls overestimated by +2.62pp on average (p<0.001)
- **Democrats**: IVR polls showed minimal bias (+0.10pp, n.s.)
- **Partisan gap**: 2.5pp pro-Republican bias, consistent across presidential, Senate, and gubernatorial races
- **Worst in 2016**: Pro-Republican bias reached 5.7pp in presidential race (Clinton vs Trump)

**2. The "Trump Effect" in 2016 Primaries**
- IVR polls overestimated Trump by +5.6pp in the Republican primary
- Potentially related to social desirability bias (Trump voters more comfortable with automated systems)
- Democratic primaries showed no comparable Clinton or Sanders bias

**3. Coverage Crisis Compounded the Problem**
- As cell-only households grew (20% → 51%), IVR's sample became increasingly unrepresentative
- Live phone surveys could legally call cell phones; IVR could not
- Partisan bias worsened over time, correlating with cell phone adoption
- By 2016, IVR was systematically missing younger, more urban, more diverse voters

**4. Undecided Rate Finding Held**
- IVR continued to show ~2-3pp fewer undecided voters across all years
- Effect remained consistent even as coverage deteriorated
- Suggests the undecided rate difference reflects measurement, not just coverage

### Implications

The extended analysis reveals that the original thesis identified an important methodological difference, but **understated the problem**. The undecided rate finding was real and persistent, but coverage bias created a larger issue: systematic partisan bias that worsened over time.

**For poll aggregators:** Methodology adjustments are essential. Simply averaging IVR and live phone polls introduces systematic error.

**For the polling industry:** IVR's cost advantages were overwhelmed by coverage problems. By 2016, landline-only IVR was producing systematically biased estimates.

**For researchers:** Survey mode effects are not static—they evolve as technology and respondent behavior change. A finding from 2010 may not hold in 2016.

### Extended Analysis Code and Data

All extended analysis code, data, and visualizations are available in this repository:
- See `R/` directory for analysis scripts
- See `figures/` for additional visualizations
- See `results/` for regression outputs and summary statistics

---

## Citation

If you use this work, please cite:

**Original thesis (2011):**
```bibtex
@mastersthesis{brunk2011examining,
  author  = {Brunk, Alexander},
  title   = {Examining the Relationship Between Polling Methodology and Undecided Voters},
  year    = {2011},
  type    = {Master's Thesis},
  url     = {https://github.com/abrunk/thesis_ivr_polling}
}
```

**Extended analysis (2026):**
```bibtex
@misc{brunk2026ivr,
  author  = {Brunk, Alexander},
  title   = {IVR Polling Analysis: Undecided Voters and Partisan Bias (2008-2016)},
  year    = {2026},
  url     = {https://github.com/abrunk/ivr-polling-analysis}
}
```

---

## License

**Data:** Collected from public sources; original compilation © 2011 Alexander Brunk

**Code:** MIT License

**Thesis text:** © 2011 Alexander Brunk. All rights reserved.

---

## Contact

**Alexander Brunk**
GitHub: [@abrunk](https://github.com/abrunk)

---

*Original thesis completed: 2011*
*Visualizations updated: February 2026*
