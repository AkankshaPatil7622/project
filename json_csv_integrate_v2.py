import csv
import json
import requests
import pandas as pd

# Step 1: Fetch and Convert JSON to CSV
def fetch_and_convert_to_csv(thingspeak_url, output_csv_file):
    response = requests.get(thingspeak_url)
    data = response.json()
    
    # Assuming 'feeds' contains the data points
    fieldnames = list(data['feeds'][0].keys())
    
    with open(output_csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for feed in data['feeds']:
            writer.writerow(feed)
    
    print(f"Data converted to CSV and saved to {output_csv_file}")

# Step 2: Clean the CSV Data
def clean_csv_data(input_csv_file, cleaned_csv_file):
    df = pd.read_csv(input_csv_file)
    
    # Example cleaning operations:
    df.drop_duplicates(inplace=True)  # Remove duplicates
    df.ffill(inplace=True)  # Forward fill missing values
    
    df.to_csv(cleaned_csv_file, index=False)
    print(f"Cleaned data saved to {cleaned_csv_file}")

# Usage
thingspeak_url = 'https://api.thingspeak.com/channels/2057381/feeds.json?results=100'
output_csv_file = 'data.csv'
cleaned_csv_file = 'cleaned_data.csv'

fetch_and_convert_to_csv(thingspeak_url, output_csv_file)
clean_csv_data(output_csv_file, cleaned_csv_file)
