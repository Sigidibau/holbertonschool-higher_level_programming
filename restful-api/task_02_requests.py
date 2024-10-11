#!/usr/bin/python3


import csv
import requests


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
    for d in data:
        print(d['title'])
    else:
        print("Failed to retrieve data", r.status_code)

def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        data = r.json()
        list = []

    for d in data:
        list.append({
            'id': d ['id'],
            'title': d ['title'],
            'body': d ['body']
        })

        with open('d.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
                writer.writeheader()
                writer.writerows(list)

