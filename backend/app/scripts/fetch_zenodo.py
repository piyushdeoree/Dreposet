import json
import requests
from pathlib import Path

def fetch_zenodo_datasets(query: str, max_results: int = 20):
    url = "https://zenodo.org/api/records"
    params = {
        "q": query,
        "size": max_results,
        "type": "dataset",
    }

    resp = requests.get(url, params=params)
    resp.raise_for_status()
    hits = resp.json().get("hits", {}).get("hits", [])

    datasets = []
    for h in hits:
        metadata = h.get("metadata", {})
        datasets.append({
            "name": metadata.get("title", ""),
            "source": "Zenodo",
            "description": metadata.get("description", "")[:300],  # trim long HTML descriptions
            "url": h.get("links", {}).get("self_html", ""),
            "tags": metadata.get("keywords", []) or [],
        })

    return datasets

if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).resolve().parents[3]
    OUTPUT_DIR = PROJECT_ROOT / "data" / "raw"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    data = fetch_zenodo_datasets("fake news")
    output_path = OUTPUT_DIR / "zenodo_sample.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} datasets to {output_path}")