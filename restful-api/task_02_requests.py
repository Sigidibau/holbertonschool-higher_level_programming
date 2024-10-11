#!/usr/bin/python3


import csv
import requests


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
    for post in data:
        print(post['title'])
    else:
        print("Failed to retrieve data", r.status_code)

def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code for saving: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        d_list = []

    for posts in data:
        d_list.append({
            'id': posts['id'],
            'title': posts['title'],
            'body': posts['body']
        })

        with open('posts.csv', 'w', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
                writer.writeheader()
                writer.writerows(d_list)
