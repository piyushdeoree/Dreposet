import json
from pathlib import Path
from app.db.database import SessionLocal
from app.db.models import Dataset, GitHubRepo

PROJECT_ROOT = Path(__file__).resolve().parents[3]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

def load_json(filename):
    path = RAW_DIR / filename
    if not path.exists():
        print(f"Skipping {filename} (not found)")
        return []
    with open(path, "r") as f:
        return json.load(f)

def ingest_datasets(db):
    count = 0
    for filename in [
    "kaggle_sample.json",
    "huggingface_sample.json",
    "uci_sample.json",
    "openml_sample.json",
    "zenodo_sample.json",
    "worldbank_sample.json",
]:
        items = load_json(filename)
        for item in items:
            dataset = Dataset(
                name=item.get("name", ""),
                source=item.get("source", ""),
                description=item.get("description", ""),
                url=item.get("url", ""),
                format=item.get("format", ""),
                size=str(item.get("size", "")),
                tags=item.get("tags", []),
            )
            db.add(dataset)
            count += 1
    db.commit()
    print(f"Ingested {count} datasets")

def ingest_github(db):
    items = load_json("github_sample.json")
    count = 0
    for item in items:
        repo = GitHubRepo(
            name=item.get("name", ""),
            description=item.get("description", ""),
            language=item.get("language", "Unknown"),
            stars=item.get("stars", 0),
            url=item.get("url", ""),
            topics=item.get("topics", []),
        )
        db.add(repo)
        count += 1
    db.commit()
    print(f"Ingested {count} GitHub repos")

if __name__ == "__main__":
    db = SessionLocal()
    try:
        ingest_datasets(db)
        ingest_github(db)
    finally:
        db.close()