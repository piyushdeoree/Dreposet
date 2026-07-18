import requests

def fetch(query: str, max_results: int = 10):
    try:
        url = "https://www.openml.org/api/v1/json/data/list"
        resp = requests.get(url, params={"limit": 100}, timeout=5)
        all_datasets = resp.json().get("data", {}).get("dataset", [])

        query_lower = query.lower()
        datasets = []
        for d in all_datasets:
            name = d.get("name", "")
            if query_lower in name.lower():
                datasets.append({
                    "name": name,
                    "source": "OpenML",
                    "description": f"OpenML dataset (id: {d.get('did')})",
                    "url": f"https://www.openml.org/d/{d.get('did')}",
                    "tags": [],
                })
            if len(datasets) >= max_results:
                break
        return datasets
    except Exception as e:
        print(f"[OpenML] fetch failed: {e}")
        return []
    