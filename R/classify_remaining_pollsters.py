"""
Automated pipeline to classify remaining unknown pollsters
"""
import csv
import re
from collections import Counter, defaultdict

print("="*80)
print("AUTOMATED POLLSTER CLASSIFICATION PIPELINE")
print("="*80)

# Load current master mapping
current_mapping = {}
with open(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\processed\pollster_methodology_master.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pollster = row['pollster'].strip('"')
        methodology = row['methodology']
        current_mapping[pollster.lower()] = methodology

print(f"\nCurrent mapping: {len(current_mapping)} pollsters")

# ============================================================================
# STRATEGY 1: Extract comments from data files for clues
# ============================================================================
print("\n" + "="*80)
print("STRATEGY 1: Mining comment fields from data")
print("="*80)

comment_clues = defaultdict(list)

# Check 2014 TSV
print("\nChecking 2014 data...")
with open(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\raw\fivethirtyeight\raw-polls-2014.tsv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    header = next(reader)
    # Find comment column (usually last)
    for row in reader:
        if len(row) > 6:
            pollster = row[6].strip()
            if len(row) > 23 and row[23]:  # comment column
                comment = row[23].lower()
                if any(word in comment for word in ['ivr', 'automated', 'robocall', 'robo', 'live', 'telephone', 'internet', 'online']):
                    comment_clues[pollster].append(comment)

# Check 2016 CSV
print("Checking 2016 data...")
with open(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\raw\fivethirtyeight\raw-polls-2016.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if len(row) > 6:
            pollster = row[6].strip()
            if len(row) > 23 and row[23]:
                comment = row[23].lower()
                if any(word in comment for word in ['ivr', 'automated', 'robocall', 'robo', 'live', 'telephone', 'internet', 'online']):
                    comment_clues[pollster].append(comment)

# Check 2018 CSV
print("Checking 2018 data...")
with open(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\raw\fivethirtyeight\raw-polls-2018.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if len(row) > 6:
            pollster = row[6].strip()
            if len(row) > 23 and row[23]:
                comment = row[23].lower()
                if any(word in comment for word in ['ivr', 'automated', 'robocall', 'robo', 'live', 'telephone', 'internet', 'online']):
                    comment_clues[pollster].append(comment)

print(f"\nFound methodology clues for {len(comment_clues)} pollsters")
for pollster, comments in sorted(comment_clues.items())[:10]:
    print(f"  {pollster}: {comments[0][:80]}")

# ============================================================================
# STRATEGY 2: Name-based heuristics
# ============================================================================
print("\n" + "="*80)
print("STRATEGY 2: Applying name-based heuristics")
print("="*80)

heuristic_classifications = {}

# IVR indicators
ivr_patterns = [
    r'automated',
    r'robocall',
    r'robo',
    r'ivr',
    r'insider\s*advantage',
    r'opinion\s*savvy',
    r'we\s*ask\s*america',
]

# Live phone indicators
live_patterns = [
    r'university(?! of phoenix)',  # Universities usually use live interviewers
    r'college',
    r'research\s+associates',
    r'opinion\s+research',
    r'\bpoll\s+by\s+',
    r'survey\s+center',
]

# Online indicators
online_patterns = [
    r'interactive(?!.*voice)',  # Interactive but not IVR
    r'surveymonkey',
    r'panel',
    r'yougov',
    r'internet',
    r'online',
]

# Get all pollsters from our data
all_pollsters = set()
for filepath in [
    r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\raw\fivethirtyeight\2012_polls.csv',
    r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\raw\fivethirtyeight\raw-polls-2014.tsv',
    r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\raw\fivethirtyeight\raw-polls-2016.csv',
    r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\raw\fivethirtyeight\raw-polls-2018.csv',
]:
    try:
        delimiter = '\t' if 'tsv' in filepath else ','
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=delimiter)
            next(reader)
            col_idx = 0 if '2012' in filepath else 6
            for row in reader:
                if len(row) > col_idx and row[col_idx]:
                    all_pollsters.add(row[col_idx].strip())
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

print(f"\nTotal unique pollsters in data: {len(all_pollsters)}")

# Apply heuristics to unknown pollsters
for pollster in all_pollsters:
    if pollster.lower() not in current_mapping:
        pollster_lower = pollster.lower()

        # Check IVR patterns
        for pattern in ivr_patterns:
            if re.search(pattern, pollster_lower):
                heuristic_classifications[pollster] = ('IVR', f'name pattern: {pattern}')
                break

        # Check online patterns
        if pollster not in heuristic_classifications:
            for pattern in online_patterns:
                if re.search(pattern, pollster_lower):
                    heuristic_classifications[pollster] = ('Online', f'name pattern: {pattern}')
                    break

        # Check live patterns
        if pollster not in heuristic_classifications:
            for pattern in live_patterns:
                if re.search(pattern, pollster_lower):
                    heuristic_classifications[pollster] = ('Live', f'name pattern: {pattern}')
                    break

print(f"\nHeuristic classifications: {len(heuristic_classifications)}")
for pollster, (method, reason) in sorted(heuristic_classifications.items())[:20]:
    print(f"  {pollster[:40]:40s} -> {method:10s} ({reason})")

# ============================================================================
# STRATEGY 3: Improved fuzzy matching
# ============================================================================
print("\n" + "="*80)
print("STRATEGY 3: Improved fuzzy matching with aliases")
print("="*80)

# Common aliases and variations
pollster_aliases = {
    'public policy polling': ['ppp', 'ppp (d)'],
    'rasmussen reports': ['rasmussen', 'scott rasmussen'],
    'surveyusa': ['survey usa'],
    'marist college': ['marist'],
    'quinnipiac university': ['quinnipiac'],
    'university of new hampshire': ['unh'],
    'cnn/opinion research': ['cnn', 'opinion research corp'],
    'abc news/washington post': ['abc/wapo', 'abc news'],
    'cbs news/new york times': ['cbs/nyt', 'cbs news'],
    'insider advantage': ['insideradvantage', 'opinion savvy/insideradvantage'],
    'mason-dixon': ['mason dixon'],
}

# Create reverse lookup
alias_to_canonical = {}
for canonical, aliases in pollster_aliases.items():
    for alias in aliases:
        alias_to_canonical[alias.lower()] = canonical

fuzzy_matches = {}
for pollster in all_pollsters:
    pollster_lower = pollster.lower()

    # Skip if already classified
    if pollster_lower in current_mapping:
        continue

    # Check if it's an alias
    for alias, canonical in alias_to_canonical.items():
        if alias in pollster_lower or pollster_lower in alias:
            if canonical in current_mapping:
                fuzzy_matches[pollster] = (canonical, current_mapping[canonical])
                break

print(f"\nFuzzy matches found: {len(fuzzy_matches)}")
for pollster, (canonical, method) in sorted(fuzzy_matches.items())[:10]:
    print(f"  {pollster[:40]:40s} -> {canonical:30s} ({method})")

print("\n" + "="*80)
print("PIPELINE SUMMARY")
print("="*80)
print(f"Comment clues found: {len(comment_clues)}")
print(f"Heuristic classifications: {len(heuristic_classifications)}")
print(f"Fuzzy matches: {len(fuzzy_matches)}")
print(f"\nTotal new classifications: {len(heuristic_classifications) + len(fuzzy_matches)}")

# Save findings
with open(r'C:\Users\Alexander\Projects\ivr-polling-analysis\data\processed\automated_classifications.csv', 'w', newline='', encoding='utf-8') as f:
    f.write("pollster,methodology,source,notes\n")

    # Write heuristic classifications
    for pollster, (method, reason) in sorted(heuristic_classifications.items()):
        f.write(f'"{pollster}",{method},heuristic,"{reason}"\n')

    # Write fuzzy matches
    for pollster, (canonical, method) in sorted(fuzzy_matches.items()):
        f.write(f'"{pollster}",{method},fuzzy_match,"matched to: {canonical}"\n')

print("\nSaved to: automated_classifications.csv")
