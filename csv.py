#!/usr/bin/env python

import csv
import sys
import requests
import csv

def get_csvfile(url):
    r = requests.get(url)
    text = r.iter_lines()
    reader = csv.reader(text, delimiter=',')

def main():
    url = sys.argv[1]

if __name__ == "__main__":
    main()
