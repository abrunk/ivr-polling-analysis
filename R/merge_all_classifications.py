"""
Merge all classification sources into final master file
"""
import pandas as pd

print("="*80)
print("MERGING ALL POLLSTER CLASSIFICATIONS")
print("="*80)

# Read all sources
print("\nReading classification sources...")

# 1. Original master (thesis + manual research)
master_df = pd.read_csv(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\processed\pollster_methodology_master.csv')
print(f"Original master: {len(master_df)} pollsters")

# 2. Automated classifications
automated_df = pd.read_csv(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\processed\automated_classifications.csv')
print(f"Automated pipeline: {len(automated_df)} pollsters")

# 3. Web research on top 5
web_research_df = pd.read_csv(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\processed\web_research_top5.csv')
print(f"Web research (top unknowns): {len(web_research_df)} pollsters")

# Combine all
all_dfs = [master_df, automated_df, web_research_df]
combined = pd.concat(all_dfs, ignore_index=True)

# Remove exact duplicates keeping last (prioritize: original < automated < web research)
combined = combined.drop_duplicates(subset=['pollster'], keep='last')

print(f"\nCombined total: {len(combined)} pollsters")

# Count by methodology
print("\nBreakdown by methodology:")
print(combined['methodology'].value_counts())

# Save final master
output_file = r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\processed\pollster_methodology_final.csv'
combined = combined.sort_values('pollster')
combined.to_csv(output_file, index=False)

print(f"\nSaved final master file: pollster_methodology_final.csv")
print(f"  Total pollsters: {len(combined)}")

# Show special cases
print("\nSpecial classifications:")
exclude = combined[combined['methodology'] == 'Exclude']
if len(exclude) > 0:
    print(f"  TO EXCLUDE: {len(exclude)} pollsters")
    for _, row in exclude.iterrows():
        print(f"    - {row['pollster']}: {row['notes']}")

unknown = combined[combined['methodology'] == 'Unknown']
print(f"  STILL UNKNOWN: {len(unknown)} pollsters")
for _, row in unknown.head(10).iterrows():
    print(f"    - {row['pollster']}")
