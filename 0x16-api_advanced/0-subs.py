#!/usr/bin/python3
'''0-subs.py'''


def number_of_subscribers(subreddit):
    '''Function to query the REDDIT API and return #
    of subscripers for given subressit'''
    import requests

     sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
     if sub_info.status_code >= 300:
         return 0

     return sub_info.json().get("data").get("subscribers")
