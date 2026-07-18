from fastapi import APIRouter
from app.models.schemas import SearchRequest, SearchResponse
from app.services.search import search_datasets, search_github_repos
from app.services.ranking import rank_datasets, rank_github_repos
from app.services.explain import explain_dataset, explain_github_repo
from app.services.analytics import build_analytics

router = APIRouter()


@router.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):
    query = request.query

    raw_datasets = search_datasets(query, top_k=10)
    ranked_datasets = rank_datasets(query, raw_datasets)
    for d in ranked_datasets:
        d["why_recommended"] = explain_dataset(query, d)

    raw_repos = search_github_repos(query, top_k=10)
    ranked_repos = rank_github_repos(query, raw_repos)
    for r in ranked_repos:
        r["why_recommended"] = explain_github_repo(query, r)

    analytics = build_analytics(query, ranked_datasets, ranked_repos)

    return {
        "analytics": analytics,
        "datasets": ranked_datasets,
        "github_repos": ranked_repos,
    }