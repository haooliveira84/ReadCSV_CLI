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
    value = []
    with open(file) as text:
        reader = csv.reader(text, delimiter=',')
        for row in reader:
            value.append(row)
        return value

def origin(file):
    try:
        if file.startswith('htt'):
            ret = get_csvfile_remote(file)
            print ret
        else:
            ret = get_csvfile_local(file)
            return ret
    except TypeError:
        print "No CSV data recivied"
