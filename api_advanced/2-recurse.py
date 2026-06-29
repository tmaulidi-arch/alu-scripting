#!/usr/bin/python3
"""Recursive function that queries Reddit API and returns all hot titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles for a given subreddit."""
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
        return None
    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
