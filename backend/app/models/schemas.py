from pydantic import BaseModel
from typing import List, Optional


class SearchRequest(BaseModel):
    query: str


class DatasetResult(BaseModel):
    id: int
    name: str
    source: str
    description: str
    url: str
    tags: List[str] = []
    similarity: float
    final_score: float
    why_recommended: str


class GitHubResult(BaseModel):
    id: int
    name: str
    description: str
    language: str
    stars: int
    url: str
    similarity: float
    final_score: float
    why_recommended: str


class AnalyticsSummary(BaseModel):
    detected_task: str
    detected_domain: str
    datasets_found: int
    github_projects_found: int
    average_similarity: float
    sources_searched: List[str]
    dataset_source_distribution: dict
    dataset_type_distribution: dict


class SearchResponse(BaseModel):
    analytics: AnalyticsSummary
    datasets: List[DatasetResult]
    github_repos: List[GitHubResult]