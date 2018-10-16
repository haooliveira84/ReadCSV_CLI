#!/usr/bin/env python

#!/usr/bin/env python


import os
import sys
import operator
import json
import requests
import csv_reader
import json_reader

from collections import Counter

cont = Counter()

def main_process(data, idfile):
    values = []
    if idfile == 'csv':
        data = json.loads(data)
    for value in data:
        values.append((value['estado'], value['nome']))
    for estado, nome in values:
        cont[estado] += 1
        customers = sorted(cont.items())
    print(json.dumps(customers))

def recognize_file(file):
    try:
        with open(file) as unknown_file:
            opened = unknown_file.readline().rstrip()
        if opened != '[':
            idfile = "csv"
            main_process(csv_reader.origin(file), idfile)
        else:
            idfile = "json"
            main_process(json_reader.origin(file), idfile)
    except TypeError:
        raise "No data was received"

def recognize_remote_file(file):
    r = requests.get(file)
    opened = r.content
    if opened.startswith('['):
        idfile = "json"
        main_process(json_reader.origin(file), idfile)
    else:
        idfile = "csv"
        main_process(csv_reader.origin(file), idfile)
           

def main ():
    try:
        if sys.argv[1].startswith('htt'):
            recognize_remote_file(sys.argv[1])
        else:
            recognize_file(sys.argv[1])
    except (KeyboardInterrupt, SystemExit, IndexError):
        print ("No data to read")

if __name__ == "__main__":
    main()