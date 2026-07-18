import numpy as np
import faiss
from app.db.database import SessionLocal
from app.db.models import Dataset, GitHubRepo
from app.services.embeddings import embed_text


def build_index(embeddings: list):
    """Build a FAISS index from a list of embedding vectors."""
    dim = len(embeddings[0])
    index = faiss.IndexFlatIP(dim)  # inner product == cosine similarity if vectors are normalized
    matrix = np.array(embeddings, dtype="float32")
    faiss.normalize_L2(matrix)
    index.add(matrix)
    return index


def search_datasets(query: str, top_k: int = 10):
    db = SessionLocal()
    try:
        datasets = db.query(Dataset).filter(Dataset.embedding.isnot(None)).all()
        if not datasets:
            return []

        embeddings = [d.embedding for d in datasets]
        index = build_index(embeddings)

        query_vec = np.array([embed_text(query)], dtype="float32")
        faiss.normalize_L2(query_vec)

        scores, indices = index.search(query_vec, min(top_k, len(datasets)))

        results = []
        for score, idx in zip(scores[0], indices[0]):
            d = datasets[idx]
            results.append({
                "id": d.id,
                "name": d.name,
                "source": d.source,
                "description": d.description,
                "url": d.url,
                "tags": d.tags,
                "similarity": float(score),
            })
        return results
    finally:
        db.close()


def search_github_repos(query: str, top_k: int = 10):
    db = SessionLocal()
    try:
        repos = db.query(GitHubRepo).filter(GitHubRepo.embedding.isnot(None)).all()
        if not repos:
            return []

        embeddings = [r.embedding for r in repos]
        index = build_index(embeddings)

        query_vec = np.array([embed_text(query)], dtype="float32")
        faiss.normalize_L2(query_vec)

        scores, indices = index.search(query_vec, min(top_k, len(repos)))

        results = []
        for score, idx in zip(scores[0], indices[0]):
            r = repos[idx]
            results.append({
                "id": r.id,
                "name": r.name,
                "description": r.description,
                "language": r.language,
                "stars": r.stars,
                "url": r.url,
                "similarity": float(score),
            })
        return results
    finally:
        db.close()