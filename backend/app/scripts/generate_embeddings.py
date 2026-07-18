from app.db.database import SessionLocal
from app.db.models import Dataset, GitHubRepo
from app.services.embeddings import embed_text

def embed_datasets(db):
    datasets = db.query(Dataset).all()
    for d in datasets:
        text = f"{d.name}. {d.description}"
        d.embedding = embed_text(text)
    db.commit()
    print(f"Embedded {len(datasets)} datasets")

def embed_github_repos(db):
    repos = db.query(GitHubRepo).all()
    for r in repos:
        text = f"{r.name}. {r.description}"
        r.embedding = embed_text(text)
    db.commit()
    print(f"Embedded {len(repos)} GitHub repos")

if __name__ == "__main__":
    db = SessionLocal()
    try:
        embed_datasets(db)
        embed_github_repos(db)
    finally:
        db.close()
