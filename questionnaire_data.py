# This file loads data for use by the questionnaire

import streamlit as st
import csv
from itertools import groupby


# Load industries and sectors and return a list that maps sector to industries
def load_sectors_industries_csv(src, skips, col_nr_industry, col_nr_sector):
    sectors_industries = []

    # Open csv file
    with open(src, newline='', encoding="utf8") as file:
        r = csv.reader(file, delimiter=',', quotechar='"')
        for i, row in enumerate(r):
            # Skip header row(s)
            if i >= skips:
                # Combine sector and industry tuples in a list
                if row[col_nr_sector] and row[col_nr_industry] != '':
                    sectors_industries.append((row[col_nr_sector], row[col_nr_industry]))

    # Remove double values by converting to set and back to list, and then
    # sort alphabetically
    sectors_industries = sorted(list(set(sectors_industries)))

    # Create a list that has sector name as first item and a list of the
    # corresponding industries as second item
    # Such that it looks as follows: [[sector1, [industry1, industry2, etc...]], [sector2, [industry3, industry4, etc...]]]
    lst_sectors = []
    # Group industries by sector
    for sector, industries in groupby(sectors_industries, lambda x: x[0]):
        lst_industries = []
        # Add all industries of this sectors to a list
        for ind in industries:
            lst_industries.append(ind[1])
        # And combine sector and industries list
        lst_sectors.append([sector, lst_industries])

    return lst_sectors

# Returns the corresponding industries given a list of selected sectors
def get_industries_from_sectors(sectors_industries, selected_sectors):
    lst = []

    # For each selected sectors search and append the according industries
    for sector in selected_sectors:
        for i in sectors_industries:
            if i[0] == sector:
                lst.append(i[1])

    # Flatten the resulting list
    return [item for sublist in lst for item in sublist]
