"""
Combine thesis methodology mapping with new research to create master mapping file
"""
import csv
import pandas as pd

# Read original thesis mapping
thesis_df = pd.read_csv(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\processed\pollster_methodology_2010.csv')

# Read new additions
additions_df = pd.read_csv(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\processed\pollster_methodology_additions.csv')

# Rename columns to match
thesis_df = thesis_df.rename(columns={'methodology_2010': 'methodology'})
thesis_df['notes'] = ''

# Combine
combined = pd.concat([thesis_df, additions_df], ignore_index=True)

# Remove duplicates (keep additions over thesis if conflict)
combined = combined.drop_duplicates(subset=['pollster'], keep='last')

# Sort
combined = combined.sort_values('pollster')

# Save
output_file = r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\processed\pollster_methodology_master.csv'
combined.to_csv(output_file, index=False)

print(f"Master methodology mapping created: {output_file}")
print(f"Total pollsters: {len(combined)}")
print(f"\nBreakdown by methodology:")
print(combined['methodology'].value_counts())
