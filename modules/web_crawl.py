import requests
from urllib.parse import urljoin, urlparse
import re

def crawl_website(url, visited=None, depth=2):
    if visited is None:
        visited = set()
    if depth == 0 or url in visited:
        return []
    try:
        r = requests.get(url, timeout=3)
        visited.add(url)
        links = re.findall(r'href="(.*?)"', r.text)
        results = []
        for link in links:
            full_url = urljoin(url, link)
            if urlparse(full_url).netloc == urlparse(url).netloc:
                results.append(full_url)
                results += crawl_website(full_url, visited, depth-1)
        return list(set(results))
    except:
        return []

