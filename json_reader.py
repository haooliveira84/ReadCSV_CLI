#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json

def get_json_remote(file):
    json_data = requests.get(file)
    return json_data.json()

def get_json_local(file):
    with open(file, 'r') as data_file:
        json_result = json.load(data_file)
    return json_result

def origin(file):
    try:
        if file.startswith('htt'):
            return get_json_remote(file)
        else:
            return get_json_local(file)
    except TypeError:
        raise("No Json data recivied")

