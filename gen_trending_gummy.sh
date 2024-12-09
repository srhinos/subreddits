#!/bin/bash

urls=(
  "https://gummysearch.com/page-data/tools/top-subreddits/size-medium/page-data.json"
  "https://gummysearch.com/page-data/tools/top-subreddits/size-large/page-data.json"
  "https://gummysearch.com/page-data/tools/top-subreddits/size-huge/page-data.json"
)

output_dir="files"
output_file="$output_dir/gummy-growth-daily.txt"
temp_file="temp-gummy-growth-daily.txt"

# Delete the temporary file if it exists
if [ -f "$temp_file" ]; then
  rm "$temp_file"
fi

# Download content and append to the temporary file
for url in "${urls[@]}"; do
  if ! curl -s "$url" | jq -r '.result.pageContext.lists.growth_daily[].name' >> "$temp_file"; then
    echo "Failed to download or process $url"
    rm "$temp_file"
    exit 1
  fi
done

mv "$temp_file" "$output_file"
