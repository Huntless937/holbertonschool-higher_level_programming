#!/usr/bin/python3
"""Module to fetch posts from an API and save them to CSV."""
import csv
import requests


def fetch_and_print_posts():
    """Fetches and prints titles of all posts from JSONPlaceholder."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        for post in r.json():
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches posts and saves id, title, and body to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code == 200:
        posts = r.json()
        keys = ["id", "title", "body"]
        data = [{k: p[k] for k in keys} for p in posts]

        with open("posts.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
