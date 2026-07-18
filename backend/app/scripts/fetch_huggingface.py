import json
from huggingface_hub import HfApi

def fetch_hf_datasets(query: str, max_results: int = 20):
    api = HfApi()
    results = api.list_datasets(search=query, limit=max_results)

    datasets = []
    for d in results:
        datasets.append({
            "name": d.id,
            "source": "Hugging Face",
            "description": d.description or "",
            "url": f"https://huggingface.co/datasets/{d.id}",
            "tags": d.tags or [],
        })

    return datasets

if __name__ == "__main__":
    data = fetch_hf_datasets("fake news")
    with open("D:/Projects/ai-dataset-recommender/data/raw/huggingface_sample.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} datasets")