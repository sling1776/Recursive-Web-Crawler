#!/usr/bin/python3


# pip install --user requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import sys


def crawl(url, depth=0, maxdepth=3, visited=None):
    """
    Given an absolute URL, print each hyperlink found within the document.

    This is a recursive function that follows hyperlinks
    until one of two base cases are reached:

    0) No new, unvisited links are found
    1) The maximum depth of recursion is reached
    """

    if visited is None:
        visited = set()
    # Check the current depth of recursion; return now if you have gone too deep")
    if depth > maxdepth:
        return
    try:
        response = requests.get(url)
        visited.add(url)
        if not response.ok:
            print(f"crawl({url}): {response.status_code} {response.reason}")
            return
        print(("    " * depth) + url)
        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
        for a in links:
            link = a.get('href')
            if link:
                link = link.split("#")[0]
                # Create an absolute address from a (possibly) relative URL
                absoluteURL = urljoin(url, link)

                # Only deal with resources accessible over HTTP or HTTPS
                if absoluteURL.startswith('http'):
                    if absoluteURL not in visited:
                        crawl(absoluteURL, depth+1, maxdepth, visited)
    except Exception as e:
        print(f"crawl(): {e}")
    return

# ----------------START READING HERE----------------------
# An absolute URL is required to begin
if len(sys.argv) < 2:
    print("Error: no Absolute URL supplied")
    sys.exit(1)
else:
    url = sys.argv[1]

# Determine whether variable `url` contains an absolute URL
parsed = urlparse(url)
if "http" not in parsed[0] or ("." not in parsed[1]):
    print("Error: Invalid URL supplied.\nPlease supply an absolute URL to this program")
    sys.exit(1)

# If a maxDepth argument is given, then verify that it is valid and use it for the maxDepth.
if len(sys.argv) > 2:
    try:
        maxDepth = int(sys.argv[2])
    except Exception as e:
        print("User Entered a bad depth number. Reset value:MaxDepth = 3")
        maxDepth = 3
else:
    maxDepth = 3

# Format Header
plural = 's'
if maxDepth == 1:
    plural = ''

print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")
# Here we go!!!
crawl(url, maxdepth=maxDepth)
