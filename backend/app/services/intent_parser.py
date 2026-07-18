import re

TASK_KEYWORDS = {
    "Classification": ["classify", "classification", "detect", "detection", "predict whether", "spam", "fraud", "sentiment"],
    "Regression": ["predict price", "predict value", "forecast", "regression", "estimate the", "housing price"],
    "Clustering": ["cluster", "clustering", "segment", "segmentation", "group similar"],
    "Computer Vision": ["image", "images", "vision", "object detection", "photo", "video", "face recognition"],
    "NLP": ["text", "sentiment", "language", "nlp", "news", "chatbot", "translation", "summarization"],
    "Time Series": ["time series", "forecast", "stock price", "trend over time"],
    "Recommendation": ["recommend", "recommendation", "suggest products", "personaliz"],
}

DOMAIN_KEYWORDS = {
    "Finance": ["loan", "credit", "bank", "stock", "finance", "fraud", "trading", "investment"],
    "Healthcare": ["patient", "disease", "medical", "diagnosis", "health", "hospital", "symptom"],
    "Natural Language Processing": ["news", "text", "sentiment", "language", "chatbot", "review", "article"],
    "E-commerce": ["product", "customer", "purchase", "e-commerce", "shopping", "retail"],
    "Computer Vision": ["image", "video", "face", "object detection", "photo"],
    "Social Media": ["twitter", "social media", "post", "tweet", "instagram", "facebook"],
    "Transportation": ["traffic", "vehicle", "accident", "transportation", "road"],
}


def detect_task(query: str) -> str:
    query_lower = query.lower()
    for task, keywords in TASK_KEYWORDS.items():
        for kw in keywords:
            if kw in query_lower:
                return task
    return "General / Unspecified"


def detect_domain(query: str) -> str:
    query_lower = query.lower()
    for domain, keywords in DOMAIN_KEYWORDS.items():
        for kw in keywords:
            if kw in query_lower:
                return domain
    return "General"


def extract_keywords(query: str, max_keywords: int = 6) -> list:
    # Simple stopword-based keyword extraction, no ML needed
    stopwords = {
        "i", "want", "to", "build", "a", "an", "the", "for", "of", "and", "that",
        "using", "with", "is", "in", "on", "system", "model", "project", "my",
    }
    words = re.findall(r"[a-zA-Z]+", query.lower())
    keywords = [w for w in words if w not in stopwords and len(w) > 2]
    # Deduplicate while preserving order
    seen = set()
    result = []
    for w in keywords:
        if w not in seen:
            seen.add(w)
            result.append(w)
    return result[:max_keywords]


def parse_intent(query: str) -> dict:
    return {
        "task": detect_task(query),
        "domain": detect_domain(query),
        "keywords": extract_keywords(query),
    }