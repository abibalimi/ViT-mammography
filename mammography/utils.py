#!/usr/env/bin python3

import csv
from typing import List, Dict
def dict_to_csv(dico: List[Dict[str, str]], headers: List[str], file_name: str = 'raw_data/annotations.csv'):
    """Writes a list of dictionaries to a CSV file.

    Args:
        dico (List[Dict[str, str]]): Data to be written to CSV.
        headers (List[str]): Column headers.
        file_name (str): Output file path.
    """
    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(dico)
        print(f"✅ Successfully saved: {file_name}")  # Success logging
    except Exception as e:
        print(f"❌ Error writing CSV: {e}")  # Error handling
    

if __name__ == "__main__":
    cars = [
        {"images": 1, "labels": "MLO"},
        {"images": 2, "labels": "CC"},
        ]
    headers = ["images", "labels"]
    dict_to_csv(cars, headers)