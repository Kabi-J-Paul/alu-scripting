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
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))
    if data.get("after"):
        return recurse(subreddit, hot_list, data.get("after"))
    return hot_list if hot_list else None
