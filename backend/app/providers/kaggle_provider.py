import os
from dotenv import load_dotenv
load_dotenv()

from kaggle.api.kaggle_api_extended import KaggleApi

def fetch(query: str, max_results: int = 10):
    try:
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
                "tags": [t.name for t in getattr(d, "tags", [])] if hasattr(d, "tags") else [],
            })
        return datasets
    except Exception as e:
        print(f"[Kaggle] fetch failed: {e}")
        return []