#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

#!/usr/bin/env python


import os
import sys
import operator
import json
import csv_reader
import json_reader

from collections import Counter

cont = Counter()

def main_process(data):
    values = []
    data = sorted(data, key=lambda k: k['estado'])
    for value in data:
        values.append((value['estado'], value['nome']))
    for estado, nome in values:
        cont[estado] += 1
        customers = sorted(cont.items())
    return jsonify(customers)

def recognize_file(file):
    try:
        with open(file) as unknown_file:
            opened = unknown_file.read(1)
            if opened != '[':
                csv_reader.origin(file)
            else:
                json_reader.origin(file)
    except TypeError:
        print "No data was receivied"

def main ():
    file = sys.argv[1]
    recognize_file(file)

if __name__ == "__main__":
    main()
