import requests

def fetch(query: str, max_results: int = 10):
    try:
        url = "https://api.worldbank.org/v2/indicator"
        resp = requests.get(url, params={"format": "json", "per_page": 300}, timeout=5)
        result = resp.json()
        if len(result) < 2:
            return []

        indicators = result[1]
        query_lower = query.lower()
        datasets = []
        for ind in indicators:
            name = ind.get("name", "")
            if query_lower in name.lower():
                datasets.append({
                    "name": name,
                    "source": "World Bank",
                    "description": (ind.get("sourceNote") or "")[:300],
                    "url": f"https://data.worldbank.org/indicator/{ind.get('id')}",
                    "tags": [],
                })
            if len(datasets) >= max_results:
                break
        return datasets
    except Exception as e:
        print(f"[World Bank] fetch failed: {e}")
        return []
    