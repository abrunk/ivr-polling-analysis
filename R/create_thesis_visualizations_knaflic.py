"""
Create Thesis Visualizations Using Cole Knaflic Principles
Focus on clear, simple, story-driven visualizations

Key Principles:
1. Remove clutter - eliminate unnecessary elements
2. Focus attention - use pre-attentive attributes strategically
3. Think like a designer - alignment, white space, contrast
4. Tell a story - titles that state the finding
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set clean, minimal style
sns.set_style("white")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

print("=" * 80)
print("CREATING THESIS VISUALIZATIONS (Cole Knaflic Principles)")
print("=" * 80)

# Load thesis data from original repository
thesis = pd.read_csv(r'C:\Users\Alexander\Projects\thesis_ivr_polling\Data\2010 Undecideds Data - Cleaned CSV.csv')
thesis_clean = thesis[thesis['Survey_Type'].isin(['Live', 'IVR'])].copy()

print(f"\nTotal polls: {len(thesis_clean)}")
print(f"  Live: {len(thesis_clean[thesis_clean['Survey_Type']=='Live'])}")
print(f"  IVR:  {len(thesis_clean[thesis_clean['Survey_Type']=='IVR'])}")

# Prepare data
data = thesis_clean.copy()
data['Undecided'] = data['Modified Undecided']
data['Days'] = data['Days_Between']

#==============================================================================
# FIGURE 1: Main Finding - Simple Bar Chart
# Principle: Direct comparison with minimal visual elements
#==============================================================================
print("\nCreating Figure 1: Main Finding (Simple Bar Chart)...")

fig1, ax1 = plt.subplots(figsize=(8, 6))

# Calculate means
live_mean = data[data['Survey_Type']=='Live']['Undecided'].mean()
ivr_mean = data[data['Survey_Type']=='IVR']['Undecided'].mean()

# Simple bar chart - gray for reference, color for focus
bars = ax1.bar(['Live Phone', 'IVR'],
               [live_mean, ivr_mean],
               color=['#969696', '#d73027'],  # Gray and red
               width=0.6,
               edgecolor='none')

# Add value labels
for bar, val in zip(bars, [live_mean, ivr_mean]):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.3,
            f'{val:.1f}%',
            ha='center', va='bottom', fontsize=18, fontweight='bold')

# Simple, direct title that states the finding
ax1.set_title('IVR Polls Show 2.3pp Fewer Undecided Voters\n2010 Senate and Governor Races',
             fontsize=16, fontweight='bold', pad=20, loc='left')

# Minimal y-axis
ax1.set_ylabel('Undecided Voters (%)', fontsize=13, fontweight='bold')
ax1.set_ylim(0, 14)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_linewidth(1.5)
ax1.spines['bottom'].set_linewidth(1.5)

# Remove x-axis label (obvious from context)
ax1.set_xlabel('')
ax1.tick_params(axis='both', labelsize=12)

# Add subtle difference annotation
ax1.annotate('', xy=(1, ivr_mean), xytext=(0, live_mean),
            arrowprops=dict(arrowstyle='<->', lw=2, color='#252525'))
ax1.text(0.5, (live_mean + ivr_mean)/2 - 0.5, '-2.3pp',
        ha='center', fontsize=12, fontweight='bold', color='#252525')

plt.tight_layout()
plt.savefig('C:/Users/Alexander/Projects/ivr-polling-analysis/figures/thesis_fig1_main_finding.png',
           dpi=300, bbox_inches='tight', facecolor='white')
print("  Saved: thesis_fig1_main_finding.png")

#==============================================================================
# FIGURE 2: Temporal Pattern - Line Chart
# Principle: Show the pattern over time simply
#==============================================================================
print("\nCreating Figure 2: Temporal Pattern...")

fig2, ax2 = plt.subplots(figsize=(10, 6))

# Aggregate by month
months = {
    'September': data[(data['Days'] >= 31) & (data['Days'] < 61)],
    'October': data[(data['Days'] >= 0) & (data['Days'] < 31)]
}

month_stats = []
for month_name, month_data in months.items():
    if len(month_data) > 0:
        live_data = month_data[month_data['Survey_Type']=='Live']
        ivr_data = month_data[month_data['Survey_Type']=='IVR']

        if len(live_data) > 0:
            month_stats.append({
                'Month': month_name,
                'Method': 'Live Phone',
                'Undecided': live_data['Undecided'].mean(),
                'N': len(live_data)
            })
        if len(ivr_data) > 0:
            month_stats.append({
                'Month': month_name,
                'Method': 'IVR',
                'Undecided': ivr_data['Undecided'].mean(),
                'N': len(ivr_data)
            })

month_df = pd.DataFrame(month_stats)

# Simple line chart - one gray, one colored
for method, color, zorder in [('Live Phone', '#969696', 1), ('IVR', '#d73027', 2)]:
    method_data = month_df[month_df['Method']==method]
    ax2.plot(method_data['Month'], method_data['Undecided'],
            marker='o', markersize=10, linewidth=3, color=color,
            label=method, zorder=zorder)

    # Add value labels
    for _, row in method_data.iterrows():
        ax2.text(row['Month'], row['Undecided'] + 0.5,
                f"{row['Undecided']:.1f}%",
                ha='center', fontsize=11, fontweight='bold', color=color)

# Title states the finding
ax2.set_title('IVR Consistently Shows Fewer Undecideds Throughout Campaign\nLast Two Months Before 2010 Elections',
             fontsize=16, fontweight='bold', pad=20, loc='left')

ax2.set_ylabel('Undecided Voters (%)', fontsize=13, fontweight='bold')
ax2.set_xlabel('')
ax2.set_ylim(0, 12)

# Minimal design
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_linewidth(1.5)
ax2.spines['bottom'].set_linewidth(1.5)
ax2.tick_params(axis='both', labelsize=12)
ax2.legend(frameon=False, fontsize=12, loc='upper right')

plt.tight_layout()
plt.savefig('C:/Users/Alexander/Projects/ivr-polling-analysis/figures/thesis_fig2_temporal.png',
           dpi=300, bbox_inches='tight', facecolor='white')
print("  Saved: thesis_fig2_temporal.png")

#==============================================================================
# FIGURE 3: Distribution Comparison - Simple Histograms
# Principle: Show the full distribution, not just means
#==============================================================================
print("\nCreating Figure 3: Distribution Comparison...")

fig3, ax3 = plt.subplots(figsize=(10, 6))

live_data = data[data['Survey_Type']=='Live']['Undecided']
ivr_data = data[data['Survey_Type']=='IVR']['Undecided']

# Overlapping histograms with transparency
ax3.hist(live_data, bins=15, alpha=0.5, color='#969696',
         edgecolor='black', linewidth=1.5, label=f'Live Phone (n={len(live_data)})')
ax3.hist(ivr_data, bins=15, alpha=0.5, color='#d73027',
         edgecolor='black', linewidth=1.5, label=f'IVR (n={len(ivr_data)})')

# Add mean lines
ax3.axvline(live_mean, color='#969696', linestyle='--', linewidth=3, alpha=0.8,
           label=f'Live mean: {live_mean:.1f}%')
ax3.axvline(ivr_mean, color='#d73027', linestyle='--', linewidth=3, alpha=0.8,
           label=f'IVR mean: {ivr_mean:.1f}%')

# Title states the finding
ax3.set_title('IVR Distribution More Tightly Clustered Around Lower Values\n805 Polls from 2010 Elections',
             fontsize=16, fontweight='bold', pad=20, loc='left')

ax3.set_xlabel('Undecided Voters (%)', fontsize=13, fontweight='bold')
ax3.set_ylabel('Number of Polls', fontsize=13, fontweight='bold')

# Minimal design
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['left'].set_linewidth(1.5)
ax3.spines['bottom'].set_linewidth(1.5)
ax3.tick_params(axis='both', labelsize=12)
ax3.legend(frameon=False, fontsize=11, loc='upper right')

plt.tight_layout()
plt.savefig('C:/Users/Alexander/Projects/ivr-polling-analysis/figures/thesis_fig3_distribution.png',
           dpi=300, bbox_inches='tight', facecolor='white')
print("  Saved: thesis_fig3_distribution.png")

# Print summary statistics
print("\n" + "="*80)
print("SUMMARY STATISTICS")
print("="*80)
print(f"\nLive Phone: {live_mean:.2f}% undecided (SD: {live_data.std():.2f}%, n={len(live_data)})")
print(f"IVR: {ivr_mean:.2f}% undecided (SD: {ivr_data.std():.2f}%, n={len(ivr_data)})")
print(f"Difference: {ivr_mean - live_mean:.2f}pp")

# t-test
from scipy import stats
t_stat, p_val = stats.ttest_ind(ivr_data, live_data)
print(f"\nt-test: t={t_stat:.3f}, p={p_val:.6f}")
print(f"Conclusion: {'Highly significant (p<0.001)' if p_val < 0.001 else 'Significant' if p_val < 0.05 else 'Not significant'}")

print("\n" + "="*80)
print("ALL VISUALIZATIONS CREATED")
print("="*80)
print("\nPrinciples applied:")
print("  ✓ Remove clutter - minimal gridlines, no chart junk")
print("  ✓ Focus attention - color used strategically (gray vs. red)")
print("  ✓ Think like a designer - clean alignment, white space")
print("  ✓ Tell a story - titles state the finding directly")
