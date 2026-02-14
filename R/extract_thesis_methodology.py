"""
Extract pollster-methodology mapping from 2010 thesis data
"""
import csv
import sys

# Read the thesis data
pollster_methodology = {}
duplicate_warnings = []

input_file = r'C:\Users\Alexander\Projects\thesis_ivr_polling\Data\2010 Undecideds Data - Cleaned CSV.csv'
output_file = r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\processed\pollster_methodology_2010.csv'

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pollster = row['Pollster '].strip()
        methodology = row['Survey_Type'].strip()

        # Skip if empty or invalid
        if not pollster or not methodology or methodology == 'Survey_Type':
            continue

        # Store the mapping
        if pollster in pollster_methodology:
            if pollster_methodology[pollster] != methodology:
                duplicate_warnings.append(f"WARNING: {pollster} has multiple methodologies: {pollster_methodology[pollster]} and {methodology}")
        else:
            pollster_methodology[pollster] = methodology

# Write output
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    f.write("pollster,methodology_2010,source\n")
    for pollster in sorted(pollster_methodology.keys()):
        f.write(f'"{pollster}",{pollster_methodology[pollster]},thesis_2010\n')

print(f"Extracted {len(pollster_methodology)} unique pollster-methodology mappings")
print(f"Output written to: {output_file}")

if duplicate_warnings:
    print(f"\n{len(duplicate_warnings)} warnings:")
    for warning in duplicate_warnings[:10]:
        print(f"  {warning}")
