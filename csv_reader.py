#!/usr/bin/env python

import sys
import requests
import csv

def get_csvfile_remote(file):
    r = requests.get(file)
    text = r.iter_lines()
    reader = csv.reader(text, delimiter=',')
    for row in reader:
        print row

def get_csvfile_local(file):
    with open(file) as text:
        reader = csv.reader(text, delimiter=',')
        for row in reader:
            print row

def main():
    file = sys.argv[1]
    try:
        if file.startswith('htt'):
            get_csvfile_remote(file)
        else:
            get_csvfile_local(file)
    except TypeError:
        print "No CSV data recivied"

if __name__ == "__main__":
    main()
