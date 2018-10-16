#!/usr/bin/env python

import sys
import requests
import csv
import json

def get_csvfile_remote(file):
    r = requests.get(file)
    text = r.iter_lines()
    reader = csv.DictReader(text, delimiter=',',fieldnames = ("nome","cidade","estado"))
    out = json.dumps( [ row for row in reader ] )
    return out

def get_csvfile_local(file):
    with open(file) as text:
        reader = csv.DictReader(text, delimiter=',',fieldnames = ("nome","cidade","estado"))
        out = json.dumps( [ row for row in reader ] )
    return out

def origin(file):
    try:
        if file.startswith('htt'):
            ret = get_csvfile_remote(file)
            return ret
        else:
            ret = get_csvfile_local(file)
            return ret
    except TypeError:
        print "No CSV data recivied"
