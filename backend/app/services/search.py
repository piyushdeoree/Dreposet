import numpy as np
import faiss
from app.services.embeddings import embed_text
from app.services.aggregator import fetch_all_datasets, fetch_all_github


def _build_index_and_search(items: list, query: str, top_k: int):
    if not items:
        return []

    texts = [f"{item['name']}. {item.get('description', '')}" for item in items]
    embeddings = [embed_text(t) for t in texts]

    dim = len(embeddings[0])
    index = faiss.IndexFlatIP(dim)
    matrix = np.array(embeddings, dtype="float32")
    faiss.normalize_L2(matrix)
    index.add(matrix)

    query_vec = np.array([embed_text(query)], dtype="float32")
    faiss.normalize_L2(query_vec)

    scores, indices = index.search(query_vec, min(top_k, len(items)))

    results = []
    for rank, (score, idx) in enumerate(zip(scores[0], indices[0])):
        item = dict(items[idx])
        item["id"] = rank + 1
        item["similarity"] = float(score)
        results.append(item)
    return results


def search_datasets(query: str, top_k: int = 10):
    items = fetch_all_datasets(query)
    return _build_index_and_search(items, query, top_k)


def search_github_repos(query: str, top_k: int = 10):
    items = fetch_all_github(query)
    return _build_index_and_search(items, query, top_k)