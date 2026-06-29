#!/usr/bin/python3
"""Function that queries Reddit API and prints top 10 hot posts."""
import urllib.request
import json


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "linux:alu-scripting:v1.0")
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode("utf-8"))
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
