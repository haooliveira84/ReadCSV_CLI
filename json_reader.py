#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json

def get_json_remote(file):
    json_data = requests.get(file)
    json_data
    print json_data.json()

def get_json_local(file):
    with open(file, 'r') as data_file:
        json_result = json.load(data_file)
    print json_result

def main():
    file = sys.argv[1]
    try:
        if file.startswith('htt'):
            get_json_remote(file)
        else:
            get_json_local(file)
    except TypeError:
        print "No Json data recivied"

if __name__ == "__main__":
    main()

