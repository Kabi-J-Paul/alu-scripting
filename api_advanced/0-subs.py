#!/usr/bin/python3
"""Return the number of subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return total subscribers for a subreddit, 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALU-Scripting/1.0 by Kabi-J-Paul"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data", {})
    return data.get("subscribers", 0)
