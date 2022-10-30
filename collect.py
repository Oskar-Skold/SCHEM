"""
File: collect.py
Author: Oskar Sköld
Email: oskrskld@gmail.com
Github: Oskar-Skold
Description: Collects data from different sources returns it in a standard format
"""

import requests

def get_data(url):
    # Get data from url
    data = requests.get(url)
    return data

