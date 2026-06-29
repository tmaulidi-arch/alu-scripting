#!/usr/bin/python3
"""Recursive function that counts keywords in hot articles titles."""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """Parse titles of hot articles and print sorted count of keywords."""
    if not counts:
        for word in word_list:
            word = word.lower()
            counts[word] = counts.get(word, 0)
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {
        "User-Agent": "linux:alu-scripting:v1.0 (by /u/tmaulidi-arch)"
    }
    params = {}
    if after:
        params["after"] = after
    response = requests.get(
        url, headers=headers, allow_redirects=False, params=params
    )
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")
    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1
    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
        return
    return count_words(subreddit, word_list, counts, after)
