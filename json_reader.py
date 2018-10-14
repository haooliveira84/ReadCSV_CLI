#!/usr/bin/env python

import sys
import requests
import json

def get_json_remote(file):
    print "aqui"
    r = requests.get(file)
    json_data = json.loads(r)
    print json_data.json()

def get_json_local(file):
    with open(file) as text:
        print json.dumps(text, sort_keys=True)

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

