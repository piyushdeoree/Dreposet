import requests

def fetch(query: str, max_results: int = 10):
    try:
        url = "https://zenodo.org/api/records"
        resp = requests.get(url, params={"q": query, "size": max_results, "type": "dataset"}, timeout=5)
        hits = resp.json().get("hits", {}).get("hits", [])

        datasets = []
        for h in hits:
            metadata = h.get("metadata", {})
            datasets.append({
                "name": metadata.get("title", ""),
                "source": "Zenodo",
                "description": (metadata.get("description", "") or "")[:300],
                "url": h.get("links", {}).get("self_html", ""),
                "tags": metadata.get("keywords", []) or [],
            })
        return datasets
    except Exception as e:
        print(f"[Zenodo] fetch failed: {e}")
        return []