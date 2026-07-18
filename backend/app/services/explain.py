from app.services.intent_parser import parse_intent


def explain_dataset(query: str, dataset: dict) -> str:
    intent = parse_intent(query)
    task = intent["task"]
    domain = intent["domain"]
    name = dataset.get("name", "This dataset")
    source = dataset.get("source", "")
    similarity = dataset.get("similarity", 0)

    reasons = []

    if similarity >= 0.7:
        reasons.append(f"closely matches the meaning of your query")
    elif similarity >= 0.5:
        reasons.append(f"is topically related to your query")
    else:
        reasons.append(f"shares some relevant context with your query")

    if task != "General / Unspecified":
        reasons.append(f"appears suitable for {task.lower()} tasks")

    if domain != "General":
        reasons.append(f"falls within the {domain} domain")

    explanation = f"{name} ({source}) {', and '.join(reasons)}."
    return explanation


def explain_github_repo(query: str, repo: dict) -> str:
    intent = parse_intent(query)
    task = intent["task"]
    name = repo.get("name", "This repository")
    stars = repo.get("stars", 0)
    language = repo.get("language", "Unknown")
    similarity = repo.get("similarity", 0)

    reasons = []

    if similarity >= 0.7:
        reasons.append("closely aligns with your described project")
    elif similarity >= 0.5:
        reasons.append("relates to your described project")
    else:
        reasons.append("shares some overlap with your described project")

    if task != "General / Unspecified":
        reasons.append(f"offers a reference implementation relevant to {task.lower()}")

    if stars >= 500:
        reasons.append("is a well-established, widely-used implementation")
    elif stars >= 100:
        reasons.append("has meaningful community adoption")

    explanation = f"{name} ({language}) {', and '.join(reasons)}."
    return explanation