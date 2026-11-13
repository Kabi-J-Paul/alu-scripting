#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts, None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Scripting/1.0 by Kabi-J-Paul"}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
    except Exception:
        print(None)
        return
    try:
        data = response.json()
    except Exception:
        print(None)
        return
    if not isinstance(data, dict):
        print(None)
        return
    info = data.get("data")
    children = info.get("children") if isinstance(info, dict) else None
    if not isinstance(children, list) or not children:
        print(None)
        return
    for post in children[:10]:
        detail = post.get("data") if isinstance(post, dict) else None
        title = detail.get("title") if isinstance(detail, dict) else None
        print(title)
