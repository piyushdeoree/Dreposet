from app.services.intent_parser import parse_intent


def rank_datasets(query: str, raw_results: list) -> list:
    """
    Take raw FAISS similarity results and re-rank using detected task/domain
    as a boost signal. This doesn't replace similarity — it nudges it.
    """
    intent = parse_intent(query)
    detected_task = intent["task"].lower()
    detected_domain = intent["domain"].lower()

    for r in raw_results:
        boost = 0.0
        text = f"{r.get('name', '')} {r.get('description', '')}".lower()

        # Small boost if detected task/domain words appear in the dataset's own text
        if detected_task != "general / unspecified" and detected_task in text:
            boost += 0.03
        if detected_domain != "general" and detected_domain in text:
            boost += 0.03

        # Small boost for keyword overlap
        keyword_hits = sum(1 for kw in intent["keywords"] if kw in text)
        boost += min(keyword_hits * 0.01, 0.05)  # cap keyword boost so it can't dominate

        r["final_score"] = round(r["similarity"] + boost, 4)

    # Re-sort by boosted score
    return sorted(raw_results, key=lambda x: x["final_score"], reverse=True)


def rank_github_repos(query: str, raw_results: list) -> list:
    """
    Same idea for GitHub repos, plus a small popularity nudge from stars
    (capped so it can't override relevance).
    """
    intent = parse_intent(query)
    detected_task = intent["task"].lower()
    detected_domain = intent["domain"].lower()

    max_stars = max((r.get("stars", 0) for r in raw_results), default=1) or 1

    for r in raw_results:
        boost = 0.0
        text = f"{r.get('name', '')} {r.get('description', '')}".lower()

        if detected_task != "general / unspecified" and detected_task in text:
            boost += 0.03
        if detected_domain != "general" and detected_domain in text:
            boost += 0.03

        keyword_hits = sum(1 for kw in intent["keywords"] if kw in text)
        boost += min(keyword_hits * 0.01, 0.05)

        # Small popularity nudge — normalized stars, capped at +0.03
        star_boost = min((r.get("stars", 0) / max_stars) * 0.03, 0.03)
        boost += star_boost

        r["final_score"] = round(r["similarity"] + boost, 4)

    return sorted(raw_results, key=lambda x: x["final_score"], reverse=True)