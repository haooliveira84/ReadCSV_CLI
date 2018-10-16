#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

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
    if idfile == "csv":
        data = json.dumps(data)
    for value in data:
        values.append((value['estado'], value['nome']))
    for estado, nome in values:
        cont[estado] += 1
        customers = sorted(cont.items())
    print json.dumps(customers)

def recognize_file(file):
    if file.startswith('htt'):
        file = requests.get(file, stream=True)
    try:
        with open(file) as unknown_file:
            opened = unknown_file.read(1)
            if opened != '[':
                r = csv_reader.origin(file)
                idfile = "csv"
                main_process(r, idfile)
            else:
                result = json_reader.origin(file)
                idfile = "json"
                main_process(result, idfile)
    except TypeError:
        print "No data was receivied"

def main ():
    file = sys.argv[1]
    recognize_file(file)

if __name__ == "__main__":
    main()
