#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts, None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Scripting/1.0 by Kabi-J-Paul"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    children = response.json().get("data", {}).get("children", [])
    for post in children[:10]:
        print(post.get("data", {}).get("title"))
