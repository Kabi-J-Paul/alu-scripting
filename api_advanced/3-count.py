#!/usr/bin/python3
"""Count keyword occurrences in the hot articles of a subreddit."""
import requests


def _fetch_titles(subreddit, hot_list=None, after=None):
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
        return _fetch_titles(subreddit, hot_list, info.get("after"))
    return hot_list


def count_words(subreddit, word_list):
    """Print sorted keyword counts found in hot article titles."""
    titles = _fetch_titles(subreddit)
    if not titles:
        return
    multiplicity = {}
    for word in word_list:
        key = word.lower()
        multiplicity[key] = multiplicity.get(key, 0) + 1
    found = {word: 0 for word in multiplicity}
    for title in titles:
        if not isinstance(title, str):
            continue
        for token in title.split():
            key = token.lower()
            if key in found:
                found[key] += 1
    results = []
    for word, count in found.items():
        total = count * multiplicity[word]
        if total > 0:
            results.append((word, total))
    results.sort(key=lambda item: (-item[1], item[0]))
    for word, total in results:
        print("{}: {}".format(word, total))
