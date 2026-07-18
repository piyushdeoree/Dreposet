import json
import requests
from pathlib import Path

def fetch_worldbank_indicators(query: str, max_results: int = 20):
    # World Bank's indicator search endpoint
    url = "https://api.worldbank.org/v2/indicator"
    params = {
        "format": "json",
        "per_page": 300,  # pull a batch, filter locally since search support is basic
    }

    resp = requests.get(url, params=params)
    resp.raise_for_status()
    result = resp.json()

    if len(result) < 2:
        return []

    indicators = result[1]  # World Bank wraps results as [metadata, data]
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
                "tags": [ind.get("source", {}).get("value", "")],
            })
        if len(datasets) >= max_results:
            break

    return datasets

if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).resolve().parents[3]
    OUTPUT_DIR = PROJECT_ROOT / "data" / "raw"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    data = fetch_worldbank_indicators("poverty")
    output_path = OUTPUT_DIR / "worldbank_sample.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} datasets to {output_path}")