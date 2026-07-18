import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_github_repos(query: str, max_results: int = 20):
    url = "https://api.github.com/search/repositories"
    headers = {
        "Accept": "application/vnd.github+json",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": max_results,
    }

    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    items = resp.json().get("items", [])

    repos = []
    for r in items:
        repos.append({
            "name": r["full_name"],
            "description": r.get("description") or "",
            "language": r.get("language") or "Unknown",
            "stars": r.get("stargazers_count", 0),
            "url": r["html_url"],
            "topics": r.get("topics", []),
        })

    return repos

if __name__ == "__main__":
    data = fetch_github_repos("fake news detection")
    with open("D:/Projects/ai-dataset-recommender/data/raw/github_sample.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} repos")