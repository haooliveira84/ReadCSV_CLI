#!/usr/bin/env python

import sys
import requests
import csv
import json

def get_csvfile_remote(file):
    r = requests.get(file)
    data = r.iter_lines()
    reader = csv.DictReader(data, delimiter=',',fieldnames = ("nome","cidade","estado"))
    next(reader)
    out = json.dumps( [ row for row in reader ] )
    return out

def get_csvfile_local(file):
    with open(file) as data:
        reader = csv.DictReader(data, delimiter=',',fieldnames = ("nome","cidade","estado"))
        next(reader)
        out = json.dumps( [ row for row in reader ] )
    return out

def origin(file):
    try:
        if file.startswith('htt'):
            return get_csvfile_remote(file)
        else:
            return get_csvfile_local(file)
    except TypeError:
        raise("No CSV data recivied")
