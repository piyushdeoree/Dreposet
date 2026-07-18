import os
import requests
from dotenv import load_dotenv
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch(query: str, max_results: int = 15):
    try:
        url = "https://api.github.com/search/repositories"
        headers = {"Accept": "application/vnd.github+json"}
        if GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

        params = {"q": query, "sort": "stars", "order": "desc", "per_page": max_results}
        resp = requests.get(url, headers=headers, params=params, timeout=5)
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
            })
        return repos
    except Exception as e:
        print(f"[GitHub] fetch failed: {e}")
        return []