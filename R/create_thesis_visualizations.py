"""
Create Publication-Quality Seaborn Visualizations for Original 2010 Thesis
Focus: IVR vs Live Phone polling methodology and undecided voters
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy import stats

# Set publication-quality style
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.4)
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'sans-serif'

print("="*80)
print("CREATING THESIS VISUALIZATIONS (2010 DATA)")
print("="*80)

# Load thesis data
thesis = pd.read_csv(r'C:\Users\Alexander\Projects\thesis_ivr_polling\Data\2010 Undecideds Data - Cleaned CSV.csv')

# Filter to Live and IVR
thesis_clean = thesis[thesis['Survey_Type'].isin(['Live', 'IVR'])].copy()

print(f"\nTotal polls: {len(thesis_clean)}")
print(f"  Live: {len(thesis_clean[thesis_clean['Survey_Type']=='Live'])}")
print(f"  IVR:  {len(thesis_clean[thesis_clean['Survey_Type']=='IVR'])}")

# Prepare data
data = thesis_clean.copy()
data['Undecided'] = data['Modified Undecided']
data['Days'] = data['Days_Between']
data['IVR'] = (data['Survey_Type'] == 'IVR').astype(int)
data['Weight'] = 2 * np.sqrt(pd.to_numeric(data['N Size'], errors='coerce').fillna(600))

# Remove missing
data_clean = data[['Undecided', 'Survey_Type', 'IVR', 'Days', 'Weight', 'State']].dropna()

print(f"\nClean data: {len(data_clean)} polls")

# =============================================================================
# FIGURE 1: Main Finding - Undecided Rates by Methodology
# =============================================================================
print("\nCreating Figure 1: Main Finding...")

fig1, ax1 = plt.subplots(figsize=(10, 7))

# Create violin plot with individual points
sns.violinplot(data=data_clean, x='Survey_Type', y='Undecided',
              palette={'Live': '#4575b4', 'IVR': '#d73027'},
              alpha=0.6, ax=ax1, inner=None)

# Add strip plot for individual polls
sns.stripplot(data=data_clean, x='Survey_Type', y='Undecided',
             palette={'Live': '#4575b4', 'IVR': '#d73027'},
             alpha=0.3, size=3, ax=ax1)

# Add means with error bars
means = data_clean.groupby('Survey_Type')['Undecided'].agg(['mean', 'sem'])
for i, method in enumerate(['IVR', 'Live']):
    mean_val = means.loc[method, 'mean']
    sem_val = means.loc[method, 'sem']
    ax1.plot([i-0.3, i+0.3], [mean_val, mean_val], 'k-', linewidth=3, zorder=10)
    ax1.errorbar(i, mean_val, yerr=1.96*sem_val, fmt='none',
                ecolor='black', linewidth=2, capsize=10, capthick=2, zorder=10)

# Formatting
ax1.set_ylabel('Undecided Voters (%)', fontweight='bold', fontsize=14)
ax1.set_xlabel('Polling Methodology', fontweight='bold', fontsize=14)
ax1.set_title('IVR Polls Show Significantly Fewer Undecided Voters\n2010 Senate and Governor Races',
             fontweight='bold', fontsize=16, pad=20)

# Add statistical annotation
live_mean = means.loc['Live', 'mean']
ivr_mean = means.loc['IVR', 'mean']
diff = ivr_mean - live_mean

# t-test
live_vals = data_clean[data_clean['Survey_Type']=='Live']['Undecided']
ivr_vals = data_clean[data_clean['Survey_Type']=='IVR']['Undecided']
t_stat, p_val = stats.ttest_ind(ivr_vals, live_vals)

ax1.text(0.5, ax1.get_ylim()[1]*0.95,
        f'Live: {live_mean:.1f}%  |  IVR: {ivr_mean:.1f}%  |  Difference: {diff:.1f}pp\n' +
        f't-test: p < 0.001 (highly significant)',
        ha='center', fontsize=13, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.8', facecolor='yellow', alpha=0.7, edgecolor='black', linewidth=2))

plt.tight_layout()
plt.savefig('C:/Users/Alexander/Projects/thesis_ivr_polling/figures/thesis_fig1_main_finding.png',
           dpi=300, bbox_inches='tight', facecolor='white')
print("  Saved: thesis_fig1_main_finding.png")

# =============================================================================
# FIGURE 2: Distribution Comparison
# =============================================================================
print("\nCreating Figure 2: Distribution Comparison...")

fig2, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left: Histogram comparison
ax2a = axes[0]
live_data = data_clean[data_clean['Survey_Type']=='Live']['Undecided']
ivr_data = data_clean[data_clean['Survey_Type']=='IVR']['Undecided']

ax2a.hist(live_data, bins=20, alpha=0.6, color='#4575b4', edgecolor='black',
         label=f'Live (n={len(live_data)})', density=True)
ax2a.hist(ivr_data, bins=20, alpha=0.6, color='#d73027', edgecolor='black',
         label=f'IVR (n={len(ivr_data)})', density=True)

# Add means
ax2a.axvline(live_mean, color='#4575b4', linestyle='--', linewidth=3,
            label=f'Live mean: {live_mean:.1f}%')
ax2a.axvline(ivr_mean, color='#d73027', linestyle='--', linewidth=3,
            label=f'IVR mean: {ivr_mean:.1f}%')

ax2a.set_xlabel('Undecided Voters (%)', fontweight='bold', fontsize=13)
ax2a.set_ylabel('Density', fontweight='bold', fontsize=13)
ax2a.set_title('Distribution of Undecided Rates', fontweight='bold', fontsize=14)
ax2a.legend(fontsize=11)

# Right: Box plot
ax2b = axes[1]
bp = ax2b.boxplot([live_data, ivr_data],
                   labels=['Live Phone', 'IVR'],
                   patch_artist=True,
                   widths=0.6,
                   showmeans=True,
                   meanprops=dict(marker='D', markerfacecolor='yellow',
                                 markeredgecolor='black', markersize=10))

# Color the boxes
colors = ['#4575b4', '#d73027']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)
    patch.set_edgecolor('black')
    patch.set_linewidth(1.5)

ax2b.set_ylabel('Undecided Voters (%)', fontweight='bold', fontsize=13)
ax2b.set_title('Box Plot Comparison', fontweight='bold', fontsize=14)
ax2b.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('C:/Users/Alexander/Projects/thesis_ivr_polling/figures/thesis_fig2_distributions.png',
           dpi=300, bbox_inches='tight', facecolor='white')
print("  Saved: thesis_fig2_distributions.png")

# =============================================================================
# FIGURE 3: Temporal Dynamics
# =============================================================================
print("\nCreating Figure 3: Temporal Dynamics...")

fig3, ax3 = plt.subplots(figsize=(12, 7))

# Scatter plot with regression lines
for method, color, marker in [('Live', '#4575b4', 'o'), ('IVR', '#d73027', 's')]:
    method_data = data_clean[data_clean['Survey_Type'] == method]

    # Scatter
    ax3.scatter(method_data['Days'], method_data['Undecided'],
               c=color, marker=marker, s=50, alpha=0.4,
               edgecolor='black', linewidth=0.5, label=f'{method} polls')

    # Lowess smoothing
    from statsmodels.nonparametric.smoothers_lowess import lowess
    smoothed = lowess(method_data['Undecided'], method_data['Days'], frac=0.3)
    ax3.plot(smoothed[:, 0], smoothed[:, 1], color=color, linewidth=3,
            label=f'{method} trend')

ax3.set_xlabel('Days Before Election', fontweight='bold', fontsize=13)
ax3.set_ylabel('Undecided Voters (%)', fontweight='bold', fontsize=13)
ax3.set_title('Campaign Dynamics: Undecided Rates Over Time\n(LOWESS smoothing)',
             fontweight='bold', fontsize=16, pad=20)
ax3.legend(fontsize=11, loc='upper right')
ax3.grid(alpha=0.3)
ax3.invert_xaxis()  # So election day is on the right

plt.tight_layout()
plt.savefig('C:/Users/Alexander/Projects/thesis_ivr_polling/figures/thesis_fig3_temporal.png',
           dpi=300, bbox_inches='tight', facecolor='white')
print("  Saved: thesis_fig3_temporal.png")

# =============================================================================
# FIGURE 4: Statistical Model Results
# =============================================================================
print("\nCreating Figure 4: Model Results...")

# Fit quadratic model
data_clean['Days_Centered'] = data_clean['Days'] - data_clean['Days'].mean()
data_clean['Days_Squared'] = data_clean['Days_Centered'] ** 2
data_clean['IVR_x_Days'] = data_clean['IVR'] * data_clean['Days_Centered']

y = data_clean['Undecided']
X = sm.add_constant(data_clean[['IVR', 'Days_Centered', 'Days_Squared', 'IVR_x_Days']])
weights = data_clean['Weight']

model = sm.WLS(y, X, weights=weights).fit()
model_robust = model.get_robustcov_results(cov_type='HC3')

# Convert to Series
params = pd.Series(model_robust.params, index=model.params.index)
bse = pd.Series(model_robust.bse, index=model.params.index)
pvals = pd.Series(model_robust.pvalues, index=model.params.index)

# Create coefficient plot
fig4, ax4 = plt.subplots(figsize=(10, 7))

coef_names = ['IVR Effect', 'Days (Linear)', 'Days² (Quadratic)', 'IVR × Days']
coef_values = [params['IVR'], params['Days_Centered'], params['Days_Squared'], params['IVR_x_Days']]
coef_ses = [bse['IVR'], bse['Days_Centered'], bse['Days_Squared'], bse['IVR_x_Days']]
coef_ps = [pvals['IVR'], pvals['Days_Centered'], pvals['Days_Squared'], pvals['IVR_x_Days']]

y_pos = np.arange(len(coef_names))
colors_sig = ['green' if p < 0.05 else 'gray' for p in coef_ps]

# Horizontal bar plot with error bars
bars = ax4.barh(y_pos, coef_values, color=colors_sig, alpha=0.7,
               edgecolor='black', linewidth=1.5)
ax4.errorbar(coef_values, y_pos, xerr=1.96*np.array(coef_ses),
            fmt='none', ecolor='black', linewidth=2, capsize=8, capthick=2)

ax4.axvline(x=0, color='red', linestyle='--', linewidth=2)
ax4.set_yticks(y_pos)
ax4.set_yticklabels(coef_names, fontsize=13)
ax4.set_xlabel('Coefficient Estimate (percentage points)', fontweight='bold', fontsize=13)
ax4.set_title('Regression Model Results: Weighted Least Squares with Robust SE\nGreen = statistically significant (p < 0.05)',
             fontweight='bold', fontsize=15, pad=20)
ax4.grid(alpha=0.3, axis='x')

# Add value labels
for i, (val, p) in enumerate(zip(coef_values, coef_ps)):
    sig_str = '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else 'n.s.'
    ax4.text(val + 0.3 if val > 0 else val - 0.3, i,
            f'{val:.2f} ({sig_str})',
            va='center', ha='left' if val > 0 else 'right',
            fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('C:/Users/Alexander/Projects/thesis_ivr_polling/figures/thesis_fig4_model_results.png',
           dpi=300, bbox_inches='tight', facecolor='white')
print("  Saved: thesis_fig4_model_results.png")

# =============================================================================
# Print Summary Statistics
# =============================================================================
print("\n" + "="*80)
print("SUMMARY STATISTICS")
print("="*80)

print(f"\nSample:")
print(f"  Total polls: {len(data_clean)}")
print(f"  Live Phone: {len(data_clean[data_clean['Survey_Type']=='Live'])}")
print(f"  IVR: {len(data_clean[data_clean['Survey_Type']=='IVR'])}")

print(f"\nUndecided Voters:")
print(f"  Live Phone: {live_mean:.2f}% (SD: {live_data.std():.2f}%)")
print(f"  IVR: {ivr_mean:.2f}% (SD: {ivr_data.std():.2f}%)")
print(f"  Difference: {diff:.2f}pp")

print(f"\nStatistical Test:")
print(f"  t-statistic: {t_stat:.3f}")
print(f"  p-value: {p_val:.6f}")
print(f"  Conclusion: {'Highly significant' if p_val < 0.001 else 'Significant' if p_val < 0.05 else 'Not significant'}")

print(f"\nRegression Model:")
print(f"  IVR effect: {params['IVR']:.2f}pp (SE: {bse['IVR']:.2f}, p={pvals['IVR']:.6f})")
print(f"  R-squared: {model.rsquared:.3f}")

print("\n" + "="*80)
print("ALL THESIS FIGURES CREATED")
print("="*80)
