import requests
from bs4 import BeautifulSoup

def fetch(query: str, max_results: int = 10):
    try:
        url = f"https://archive.ics.uci.edu/datasets?search={query.replace(' ', '+')}"
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.text, "lxml")

        datasets = []
        cards = soup.select("a[href^='/dataset/']")[:max_results]
        for c in cards:
            name = c.get_text(strip=True)
            if name:
                datasets.append({
                    "name": name,
                    "source": "UCI",
                    "description": "",
                    "url": "https://archive.ics.uci.edu" + c["href"],
                    "tags": [],
                })
        return datasets
    except Exception as e:
        print(f"[UCI] fetch failed: {e}")
        return []
