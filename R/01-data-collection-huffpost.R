# Data Collection: HuffPost Pollster API (2006-2012)
#
# This script collects polling data from the HuffPost Pollster API for the
# 2006, 2008, 2010, and 2012 election cycles (gubernatorial and Senate races)
#
# API Documentation: https://app.swaggerhub.com/api/huffpostdata/pollster-api/

library(tidyverse)
library(httr)
library(jsonlite)

# Set up output directory
output_dir <- here::here("data/raw/huffpost")
if (!dir.exists(output_dir)) dir.create(output_dir, recursive = TRUE)

# HuffPost Pollster API base URL
api_base <- "http://elections.huffingtonpost.com/pollster/api/v2"

# Function to query HuffPost Pollster API for a specific race
get_huffpost_polls <- function(year, office_type = c("senate", "governor")) {
  office_type <- match.arg(office_type)

  # Build API endpoint
  # Note: The exact API structure may need adjustment based on actual API docs
  url <- paste0(api_base, "/charts/", year, "-", office_type)

  message(sprintf("Fetching %s %s polls...", year, office_type))

  # Make API request
  response <- GET(url)

  # Check for errors
  if (status_code(response) != 200) {
    warning(sprintf("Failed to fetch %s %s: Status %d",
                    year, office_type, status_code(response)))
    return(NULL)
  }

  # Parse JSON
  content <- content(response, as = "text", encoding = "UTF-8")
  data <- fromJSON(content)

  return(data)
}

# NOTE: The pollstR package may be deprecated/no longer maintained
# Check if it's available, otherwise we'll use direct API calls

if (require(pollstR)) {
  # If pollstR is available, use it
  message("Using pollstR package for data collection")

  # Example usage (will need to adapt based on actual API):
  # charts <- pollster_charts()
  # Filter for relevant years and races

} else {
  # Use direct API calls
  message("pollstR not available, using direct API calls")

  # Collect data for each cycle
  years <- c(2006, 2008, 2010, 2012)
  office_types <- c("senate", "governor")

  all_polls <- list()

  for (year in years) {
    for (office in office_types) {
      key <- paste(year, office, sep = "_")
      all_polls[[key]] <- get_huffpost_polls(year, office)

      # Be nice to the API - wait between requests
      Sys.sleep(1)
    }
  }

  # Save raw API responses
  saveRDS(all_polls, file.path(output_dir, "huffpost_raw_api_responses.rds"))
  message(sprintf("Saved raw API responses to %s", output_dir))
}

# TODO:
# 1. Test API endpoints to confirm structure
# 2. Extract poll-level data from API responses
# 3. Standardize column names to match FiveThirtyEight structure
# 4. Save as CSV files for each year

message("Data collection script created. Manual testing required before execution.")
