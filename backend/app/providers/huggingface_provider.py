from huggingface_hub import HfApi

def fetch(query: str, max_results: int = 10):
    try:
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
    except Exception as e:
        print(f"[HuggingFace] fetch failed: {e}")
        return []