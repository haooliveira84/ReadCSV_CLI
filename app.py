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
    print json.dumps(customers)

def recognize_file(file):
    try:
        if file.startswith('htt'):
            data = requests.get(file)
            with open(data) as unknown_data:
                opened = unknown_data.read(1)
                print opened
        with open(file) as unknown_file:
            opened = unknown_file.read(1)
            if opened != '[':
                idfile = "csv"
                main_process(csv_reader.origin(file), idfile)
            else:
                idfile = "json"
                main_process(json_reader.origin(file), idfile)
    except TypeError:
        print "No data was receivied"

def main ():
    try:
        recognize_file(sys.argv[1])
    except (KeyboardInterrupt, SystemExit, IndexError):
        print "No data to read"

if __name__ == "__main__":
    main()
