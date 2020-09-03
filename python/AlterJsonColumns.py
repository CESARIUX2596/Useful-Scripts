#!/usr/bin/python3


"""
 ****************************** THIS SCRIPT ALTERS JSON COLUMS******************************
"""

import json

for n in range(700):
    with open(('Documento{}.json'.format(n+1)), 'r') as jsonFile:
        data = json.load(jsonFile)
        data['title'] = 'Documento{}'.format(n+1)  # <--- add `id` value.
    with open("replayScript.json", "w") as jsonFile:
        json.dump(data, jsonFile)
