"""
Analyze pollster coverage across 2012-2018 data and match with thesis mappings
"""
import csv
from collections import Counter

# Read thesis methodology mappings
thesis_map = {}
with open(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\processed\pollster_methodology_2010.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pollster = row['pollster'].strip('"')
        methodology = row['methodology_2010']
        thesis_map[pollster.lower()] = methodology

# Count pollsters across all datasets
all_pollsters = Counter()

# 2012 data (column 1 = pollster_name)
with open(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\raw\fivethirtyeight\2012_polls.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        if len(row) > 0 and row[0]:
            all_pollsters[row[0].strip()] += 1

# 2014 data (TSV, column 7 = pollster)
with open(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\raw\fivethirtyeight\raw-polls-2014.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)  # skip header
    for row in reader:
        if len(row) > 6 and row[6]:
            all_pollsters[row[6].strip()] += 1

# 2016 data (CSV, column 7 = pollster)
with open(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\raw\fivethirtyeight\raw-polls-2016.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        if len(row) > 6 and row[6]:
            all_pollsters[row[6].strip()] += 1

# 2018 data (CSV, column 7 = pollster)
with open(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\raw\fivethirtyeight\raw-polls-2018.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        if len(row) > 6 and row[6]:
            all_pollsters[row[6].strip()] += 1

print(f"Total unique pollsters in 2012-2018: {len(all_pollsters)}")
print(f"Total polls: {sum(all_pollsters.values())}")
print("\nTop 50 pollsters by poll count:")
print("="*80)

matched = 0
unmatched = 0
matched_polls = 0
unmatched_polls = 0

for pollster, count in all_pollsters.most_common(50):
    # Try exact match first, then case-insensitive
    methodology = "Unknown"
    if pollster in thesis_map:
        methodology = thesis_map[pollster]
        matched += 1
        matched_polls += count
    elif pollster.lower() in thesis_map:
        methodology = thesis_map[pollster.lower()]
        matched += 1
        matched_polls += count
    else:
        # Try partial matching for variants
        for thesis_pollster in thesis_map.keys():
            if thesis_pollster.lower() in pollster.lower() or pollster.lower() in thesis_pollster.lower():
                methodology = f"{thesis_map[thesis_pollster]} (fuzzy)"
                matched += 1
                matched_polls += count
                break
        else:
            unmatched += 1
            unmatched_polls += count

    print(f"{count:5d}  {methodology:15s}  {pollster}")

print("\n" + "="*80)
print(f"Top 50 pollsters:")
print(f"  Matched to thesis: {matched}/50 ({matched*100/50:.1f}%)")
print(f"  Polls covered: {matched_polls}/{sum(c for p,c in all_pollsters.most_common(50))} ({matched_polls*100/sum(c for p,c in all_pollsters.most_common(50)):.1f}%)")
