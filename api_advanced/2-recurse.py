#!/usr/bin/python3
"""Return the titles of all hot articles of a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return all hot titles via recursive pagination, None if invalid."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Scripting/1.0 by Kabi-J-Paul"}
    params = {"after": after} if after else {}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
    except Exception:
        return None
    try:
        data = response.json()
    except Exception:
        return None
    if not isinstance(data, dict):
        return None
    info = data.get("data")
    children = info.get("children") if isinstance(info, dict) else None
    if not isinstance(children, list):
        return None
    for child in children:
        detail = child.get("data") if isinstance(child, dict) else None
        if isinstance(detail, dict):
            hot_list.append(detail.get("title"))
    if isinstance(info, dict) and info.get("after"):
        return recurse(subreddit, hot_list, info.get("after"))
    return hot_list if hot_list else None
