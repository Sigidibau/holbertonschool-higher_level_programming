#!/usr/bin/python3


import csv
import requests


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        posts = r.json()
    for post in posts:
        print(post['title'])
    else:
        print("Failed to retrieve data", r.status_code)

def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code for saving: {r.status_code}")
    if r.status_code == 200:
        posts = r.json()
        d_list = []

    for post in posts:
        d_list.append({
            'id': post['id'],
            'title': post['title'],
            'body': post['body']
        })

        with open('post.csv', 'w', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
                writer.writeheader()
                writer.writerows(d_list)
