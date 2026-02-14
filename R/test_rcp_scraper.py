"""
Test script to check RealClearPolitics data availability for 2012
"""

import sys
from rcp import get_polls

# Test 1: Try to search for 2012 polls
print("=" * 60)
print("Testing RealClearPolitics Python package")
print("=" * 60)

# The realclearpolitics package typically works with URLs
# Let's test if we can construct URLs for 2012 races

# Example 2012 Senate race URLs (these are guesses based on RCP's URL structure)
test_urls = [
    "https://www.realclearpolitics.com/epolls/2012/senate/ma/massachusetts_senate_brown_vs_warren-2093.html",
    "https://www.realclearpolitics.com/epolls/2012/senate/oh/ohio_senate_mandel_vs_brown-2809.html",
    "https://www.realclearpolitics.com/epolls/2012/senate/va/virginia_senate_allen_vs_kaine-2676.html"
]

print("\nTest 1: Attempting to fetch data from known 2012 Senate race URLs...")

from rcp import get_poll_data

for url in test_urls[:1]:  # Test just one to start
    try:
        print(f"\nTrying: {url}")
        data = get_poll_data(url)
        if data:
            print("SUCCESS! Sample data:")
            print(data[:200] if isinstance(data, str) else data)
            break
    except Exception as e:
        print(f"Error: {e}")

print("\n" + "=" * 60)
print("Note: The realclearpolitics package may require specific URL formats")
print("and may not work with historical data if RCP has changed their site structure")
print("=" * 60)
