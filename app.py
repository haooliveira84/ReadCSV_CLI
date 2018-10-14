#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import operator
import json

from collections import Counter

cont = Counter()

def main_process(json_data):
    values = []
    data = sorted(json_data, key=lambda k: k['estado'])
    for value in data:
        values.append((value['estado'], value['nome']))
    for estado, nome in values:
        cont[estado] += 1
        customers = sorted(cont.items())
    return jsonify(customers)

if __name__ == "__main__":
    main()
