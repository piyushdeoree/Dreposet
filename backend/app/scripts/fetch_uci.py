import json
import requests
from bs4 import BeautifulSoup

def fetch_uci_datasets(query: str, max_results: int = 20):
    url = f"https://archive.ics.uci.edu/datasets?search={query.replace(' ', '+')}"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "lxml")

    datasets = []
    cards = soup.select("a[href^='/dataset/']")[:max_results]

    for c in cards:
        name = c.get_text(strip=True)
        link = "https://archive.ics.uci.edu" + c["href"]
        if name:
            datasets.append({
                "name": name,
                "source": "UCI",
                "description": "",
                "url": link,
                "tags": [],
            })

    return datasets

if __name__ == "__main__":
    data = fetch_uci_datasets("classification")
    with open("D:/Projects/ai-dataset-recommender/data/raw/uci_sample.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} datasets")

    