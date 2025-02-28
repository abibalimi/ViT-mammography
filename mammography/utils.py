#!/usr/env/bin python3

import csv


def dict_to_csv(dico, headers):
    
    with open('raw_data/Names.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(dico)
    
if __name__ == "__main__":
    cars = [
        {"images": 1, "labels": "MLO"},
        {"images": 2, "labels": "CC"},
        ]
    headers = ["images", "labels"]
    dict_to_csv(cars, headers)