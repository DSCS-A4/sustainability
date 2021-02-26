# This file loads data for use by the questionnaire

import streamlit as st
import csv
import yfinance as yf

# Load categories based on a csv file and column number
def load_categories_csv(src, skips, col_nr):
    categories = []

    # Open csv file
    with open(src, newline='') as file:
        r = csv.reader(file, delimiter=',', quotechar='"')
        for i, row in enumerate(r):
            # Skip header row(s)
            if i >= skips:
                # Skip empty cells
                if row[col_nr] != '':
                    categories.append(row[col_nr])

    # Remove double values by converting to set and back to list, and then
    # sort alphabetically
    return sorted(list(set(categories)))
