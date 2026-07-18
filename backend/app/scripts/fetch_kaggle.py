import os
import json
from dotenv import load_dotenv

load_dotenv()  # must run BEFORE importing/using KaggleApi

from kaggle.api.kaggle_api_extended import KaggleApi

def fetch_kaggle_datasets(query: str, max_results: int = 20):
    api = KaggleApi()
    api.authenticate()

    results = api.dataset_list(search=query)
    datasets = []

    for d in results[:max_results]:
        datasets.append({
            "name": d.title,
            "source": "Kaggle",
            "description": getattr(d, "subtitle", "") or "",
            "url": f"https://www.kaggle.com/datasets/{d.ref}",
            "size": getattr(d, "totalBytes", None),
            "tags": [t.name for t in getattr(d, "tags", [])] if hasattr(d, "tags") else [],
        })

    return datasets

if __name__ == "__main__":
    data = fetch_kaggle_datasets("fake news detection")
    with open("D:/Projects/ai-dataset-recommender/data/raw/kaggle_sample.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} datasets")