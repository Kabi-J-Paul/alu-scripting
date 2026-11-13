#!/usr/bin/python3
"""Return the number of subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return total subscribers for a subreddit, 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALU-Scripting/1.0 by Kabi-J-Paul"}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
    except Exception:
        return 0
    try:
        data = response.json()
    except Exception:
        return 0
    if not isinstance(data, dict):
        return 0
    info = data.get("data")
    if not isinstance(info, dict):
        return 0
    return info.get("subscribers", 0)
