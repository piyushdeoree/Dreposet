import json
import requests
from pathlib import Path

def fetch_openml_datasets(query: str, max_results: int = 20):
    # OpenML's search endpoint filters by tag/name; we fetch a batch and filter locally
    # since their free-text search support is limited.
    url = "https://www.openml.org/api/v1/json/data/list"
    params = {"limit": 100}  # pull a batch, then filter by query below

    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()

    all_datasets = data.get("data", {}).get("dataset", [])
    query_lower = query.lower()

    datasets = []
    for d in all_datasets:
        name = d.get("name", "")
        if query_lower in name.lower():
            datasets.append({
                "name": name,
                "source": "OpenML",
                "description": f"OpenML dataset (id: {d.get('did')}), format: {d.get('format', '')}",
                "url": f"https://www.openml.org/d/{d.get('did')}",
                "format": d.get("format", ""),
                "tags": [],
            })
        if len(datasets) >= max_results:
            break

    return datasets

if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).resolve().parents[3]
    OUTPUT_DIR = PROJECT_ROOT / "data" / "raw"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    data = fetch_openml_datasets("credit")
    output_path = OUTPUT_DIR / "openml_sample.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} datasets to {output_path}")