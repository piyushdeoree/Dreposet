from collections import Counter
from app.services.intent_parser import parse_intent


def build_analytics(query: str, ranked_datasets: list, ranked_repos: list) -> dict:
    intent = parse_intent(query)

    all_similarities = [d["similarity"] for d in ranked_datasets] + [r["similarity"] for r in ranked_repos]
    avg_similarity = round(sum(all_similarities) / len(all_similarities), 3) if all_similarities else 0.0

    source_counts = Counter(d["source"] for d in ranked_datasets)
    sources_searched = list(source_counts.keys())

    # Rough "type" bucket based on detected task, since we don't have per-dataset task classification yet
    type_distribution = {intent["task"]: len(ranked_datasets)} if ranked_datasets else {}

    return {
        "detected_task": intent["task"],
        "detected_domain": intent["domain"],
        "datasets_found": len(ranked_datasets),
        "github_projects_found": len(ranked_repos),
        "average_similarity": avg_similarity,
        "sources_searched": sources_searched,
        "dataset_source_distribution": dict(source_counts),
        "dataset_type_distribution": type_distribution,
    }