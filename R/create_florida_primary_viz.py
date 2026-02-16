"""
Florida Republican Senate Primary Visualization
2010: Marco Rubio vs. Charlie Crist

Using Cole Knaflic principles for clean, story-driven visualization
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set clean style
sns.set_style("white")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

print("="*80)
print("FLORIDA REPUBLICAN SENATE PRIMARY (2010)")
print("="*80)

# Load Florida primary data
df = pd.read_excel(r'C:\Users\Alexander\Projects\thesis_ivr_polling\Data\Florida Senate Primary Data.xlsx')

# Add method labels
df['Method'] = df['Survey_Type'].map({1: 'IVR', 0: 'Live Phone'})

print(f"\nTotal polls: {len(df)}")
print(f"  IVR: {len(df[df['Method']=='IVR'])}")
print(f"  Live Phone: {len(df[df['Method']=='Live Phone'])}")

# Calculate averages by method
ivr_data = df[df['Method']=='IVR']
live_data = df[df['Method']=='Live Phone']

rubio_ivr = ivr_data['Rubio '].mean()
rubio_live = live_data['Rubio '].mean()
crist_ivr = ivr_data['Crist '].mean()
crist_live = live_data['Crist '].mean()
undc_ivr = ivr_data['Mod_Undc'].mean()
undc_live = live_data['Mod_Undc'].mean()

print(f"\nRubio:")
print(f"  IVR: {rubio_ivr:.1f}%")
print(f"  Live: {rubio_live:.1f}%")
print(f"  Difference: {rubio_ivr - rubio_live:+.1f}pp")

print(f"\nCrist:")
print(f"  IVR: {crist_ivr:.1f}%")
print(f"  Live: {crist_live:.1f}%")
print(f"  Difference: {crist_ivr - crist_live:+.1f}pp")

print(f"\nUndecided:")
print(f"  IVR: {undc_ivr:.1f}%")
print(f"  Live: {undc_live:.1f}%")
print(f"  Difference: {undc_ivr - undc_live:+.1f}pp")

#==============================================================================
# Create grouped bar chart comparing candidates by method
#==============================================================================
print("\nCreating visualization...")

fig, ax = plt.subplots(figsize=(10, 7))

# Data for plotting
candidates = ['Rubio\n(Tea Party)', 'Crist\n(Moderate)', 'Undecided']
ivr_vals = [rubio_ivr, crist_ivr, undc_ivr]
live_vals = [rubio_live, crist_live, undc_live]

x = np.arange(len(candidates))
width = 0.35

# Bars - gray for Live (reference), red for IVR (focus)
bars1 = ax.bar(x - width/2, live_vals, width,
               label='Live Phone', color='#969696',
               edgecolor='black', linewidth=1.5, alpha=0.8)
bars2 = ax.bar(x + width/2, ivr_vals, width,
               label='IVR', color='#d73027',
               edgecolor='black', linewidth=1.5, alpha=0.8)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.1f}%',
                ha='center', va='bottom', fontsize=12, fontweight='bold')

# Add difference annotations for Rubio and undecided
rubio_diff = rubio_ivr - rubio_live
undc_diff = undc_ivr - undc_live

# Rubio difference
if abs(rubio_diff) > 2:
    ax.annotate(f'{rubio_diff:+.1f}pp',
                xy=(0 + width/2, rubio_ivr),
                xytext=(10, 20), textcoords='offset points',
                fontsize=11, fontweight='bold', color='#d73027',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                         edgecolor='#d73027', linewidth=2),
                arrowprops=dict(arrowstyle='->', color='#d73027', lw=2))

# Undecided difference
if abs(undc_diff) > 2:
    ax.annotate(f'{undc_diff:+.1f}pp',
                xy=(2 + width/2, undc_ivr),
                xytext=(10, -30), textcoords='offset points',
                fontsize=11, fontweight='bold', color='#d73027',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                         edgecolor='#d73027', linewidth=2),
                arrowprops=dict(arrowstyle='->', color='#d73027', lw=2))

# Title states the finding
ax.set_title('IVR Showed Higher Support for Rubio, Fewer Undecideds\n2010 Florida Republican Senate Primary',
             fontsize=16, fontweight='bold', pad=20, loc='left')

ax.set_ylabel('Poll Average (%)', fontsize=13, fontweight='bold')
ax.set_xlabel('')
ax.set_xticks(x)
ax.set_xticklabels(candidates, fontsize=13)
ax.set_ylim(0, 60)

# Minimal design
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.tick_params(axis='both', labelsize=11)
ax.legend(frameon=False, fontsize=12, loc='upper right')

# Add note
ax.text(0.5, -0.12,
        f'Based on {len(ivr_data)} IVR polls and {len(live_data)} live phone polls conducted Jan-Aug 2010',
        ha='center', transform=ax.transAxes, fontsize=10, style='italic', color='#525252')

plt.tight_layout()
plt.savefig('C:/Users/Alexander/Projects/ivr-polling-analysis/figures/thesis_fig4_florida_primary.png',
           dpi=300, bbox_inches='tight', facecolor='white')

print("Saved: thesis_fig4_florida_primary.png")
print("\n" + "="*80)
print("VISUALIZATION COMPLETE")
print("="*80)
