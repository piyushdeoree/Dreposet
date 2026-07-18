from concurrent.futures import ThreadPoolExecutor
from app.providers import (
    kaggle_provider,
    huggingface_provider,
    uci_provider,
    openml_provider,
    zenodo_provider,
    worldbank_provider,
    github_provider,
)
from app.services.intent_parser import extract_keywords

DATASET_PROVIDERS = [
    kaggle_provider,
    huggingface_provider,
    uci_provider,
    openml_provider,
    zenodo_provider,
    worldbank_provider,
]


def _build_search_query(user_query: str) -> str:
    keywords = extract_keywords(user_query, max_keywords=5)
    return " ".join(keywords) if keywords else user_query


def fetch_all_datasets(query: str, per_source: int = 8):
    search_query = _build_search_query(query)
    results = []
    with ThreadPoolExecutor(max_workers=len(DATASET_PROVIDERS)) as executor:
        futures = [executor.submit(p.fetch, search_query, per_source) for p in DATASET_PROVIDERS]
        for f in futures:
            results.extend(f.result())
    return results


def fetch_all_github(query: str, max_results: int = 15):
    search_query = _build_search_query(query)
    return github_provider.fetch(search_query, max_results)