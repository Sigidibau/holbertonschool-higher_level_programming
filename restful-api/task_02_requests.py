#!/usr/bin/python3


import csv
import requests


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
    for i in data:
        print(data)
    else:
        print("Failed to retrieve data", r.status_code)

def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        data = r.json()
        list = []

    for x in data:
        list.append({
            'id': x ['id'],
            'title': x ['title'],
            'body': x ['body']
        })

        with open('post.csv', mode='w', newline='', encoding='utf-8') as file:
                writer= csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
                writer.writeheader()
                writer.writerows(list)
