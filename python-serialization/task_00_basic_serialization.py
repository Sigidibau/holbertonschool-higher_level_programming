#!/usr/bin/python3


import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        recive = json.dumps(data)
        f.write(recive)


def load_and_deserialize(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
