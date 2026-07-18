from app.services.search import search_datasets, search_github_repos
from app.services.ranking import rank_datasets, rank_github_repos
from app.services.explain import explain_dataset, explain_github_repo

if __name__ == "__main__":
    query = "I want to build a fake news detection model"

    raw_datasets = search_datasets(query, top_k=10)
    ranked_datasets = rank_datasets(query, raw_datasets)

    raw_repos = search_github_repos(query, top_k=10)
    ranked_repos = rank_github_repos(query, raw_repos)

    print("=== Dataset Results ===")
    for r in ranked_datasets[:5]:
        explanation = explain_dataset(query, r)
        print(f"\n{r['name']} ({r['source']}) | score: {r['final_score']:.3f}")
        print(f"  Why: {explanation}")

    print("\n=== GitHub Results ===")
    for r in ranked_repos[:5]:
        explanation = explain_github_repo(query, r)
        print(f"\n{r['name']} | score: {r['final_score']:.3f}")
        print(f"  Why: {explanation}")