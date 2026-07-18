import re

TASK_KEYWORDS = {
    "Computer Vision": [
        "image", "images", "vision", "object detection", "photo", "photos",
        "video", "face recognition", "picture", "x-ray", "scan", "mri",
        "visual", "cnn", "facial", "gesture", "ocr", "handwriting",
        "license plate", "number plate", "barcode", "qr code",
    ],
    "Classification": [
        "classify", "classification", "detect", "detection", "predict whether",
        "spam", "fraud", "sentiment", "diagnose", "diagnosis", "identify type",
        "categorize", "disease", "diseases", "default", "defaults", "predict",
        "authentic", "genuine", "verify", "screening",
    ],
    "Regression": [
        "predict price", "predict value", "forecast", "regression",
        "estimate the", "housing price", "salary prediction", "score prediction",
    ],
    "Clustering": [
        "cluster", "clustering", "segment", "segmentation", "group similar",
        "customer segmentation",
    ],
    "NLP": [
        "text", "sentiment", "language", "nlp", "news", "chatbot",
        "translation", "summarization", "speech", "transcript", "resume parser",
        "question answering", "named entity", "text generation", "essay grading",
        "plagiarism",
    ],
    "Time Series": [
        "time series", "forecast", "stock price", "trend over time",
        "demand forecasting", "sales forecasting",
    ],
    "Recommendation": [
        "recommend", "recommendation", "suggest products", "personaliz",
        "content recommendation",
    ],
    "Anomaly Detection": [
        "anomaly", "anomalies", "outlier", "intrusion detection",
        "unusual activity", "irregular", "suspicious activity",
    ],
    "Biometric / Identity": [
        "attendance", "face recognition", "fingerprint", "iris", "biometric",
        "identity verification", "face id", "voice recognition",
    ],
    "Optimization": [
        "optimize", "optimization", "scheduling", "route planning",
        "resource allocation", "load balancing",
    ],
    "Automation / Tooling": [
        "automate", "automation", "script", "cli tool", "workflow",
        "pipeline", "bot", "crawler", "scraper",
    ],
}

DOMAIN_KEYWORDS = {
    "Healthcare": [
        "patient", "disease", "diseases", "medical", "diagnosis", "diagnose",
        "health", "hospital", "symptom", "skin", "dermatology", "cancer",
        "tumor", "x-ray", "mri", "clinical", "drug", "medicine", "doctor",
    ],
    "Finance": [
        "loan", "credit", "bank", "stock", "finance", "fraud", "trading",
        "investment", "market", "currency", "insurance", "default", "defaults",
        "budget", "expense", "accounting", "invoice", "payment", "billing",
    ],
    "Natural Language Processing": [
        "news", "text", "sentiment", "language", "chatbot", "review", "article",
        "speech", "translation", "resume", "essay",
    ],
    "E-commerce / Retail": [
        "product", "customer", "purchase", "e-commerce", "shopping", "retail",
        "inventory", "order", "cart", "checkout", "warehouse",
    ],
    "Computer Vision / Imaging": [
        "image", "video", "face", "object detection", "photo", "picture",
    ],
    "Social Media": [
        "twitter", "social media", "post", "tweet", "instagram", "facebook",
        "hashtag", "influencer",
    ],
    "Transportation": [
        "traffic", "vehicle", "accident", "transportation", "road", "car",
        "driving", "collision", "parking", "fleet", "logistics", "shipment",
        "delivery route",
    ],
    "Agriculture": [
        "crop", "crops", "farm", "soil", "agriculture", "plant disease",
        "plant diseases", "leaf", "leaves", "livestock", "harvest", "irrigation",
    ],
    "Education": [
        "student", "students", "school", "college", "university", "exam",
        "grade", "grading", "course", "curriculum", "quiz", "teacher",
        "classroom", "learning management", "lms", "attendance", "e-learning",
    ],
    "Human Resources / Office": [
        "employee", "employees", "hr", "payroll", "attendance", "leave",
        "recruitment", "hiring", "interview", "onboarding", "performance review",
        "office", "workplace", "shift scheduling",
    ],
    "Software Engineering / DevOps": [
        "api", "microservice", "deployment", "ci/cd", "devops", "codebase",
        "repository", "version control", "bug tracking", "issue tracker",
        "code review", "developer tool", "ide", "compiler", "debugging",
    ],
    "Cybersecurity": [
        "security", "malware", "phishing", "intrusion", "firewall",
        "vulnerability", "encryption", "cyberattack", "authentication",
        "penetration testing",
    ],
    "IoT / Hardware": [
        "iot", "sensor", "sensors", "arduino", "raspberry pi", "embedded",
        "smart home", "wearable", "drone",
    ],
    "Gaming": [
        "game", "gaming", "player", "leaderboard", "matchmaking", "esports",
    ],
    "Environment / Climate": [
        "weather", "climate", "rain", "temperature", "pollution", "carbon",
        "sustainability", "renewable energy", "air quality", "flood",
    ],
    "Manufacturing": [
        "manufacturing", "factory", "production line", "quality control",
        "defect detection", "assembly", "supply chain",
    ],
    "Legal / Government": [
        "legal", "law", "contract", "compliance", "government", "policy",
        "regulation", "court", "voting", "census",
    ],
    "Sports": [
        "sports", "match", "player stats", "cricket", "football", "basketball",
        "tournament", "score prediction",
    ],
    "Entertainment / Media": [
        "movie", "music", "streaming", "playlist", "podcast", "content",
        "video platform",
    ],
    "Real Estate": [
        "real estate", "property", "housing", "rent", "apartment", "mortgage",
    ],
    "Biology / Genomics": [
        "gene", "genome", "dna", "rna", "protein", "cell", "biology",
        "bioinformatics",
    ],
}


def detect_task(query: str) -> str:
    query_lower = query.lower()
    scores = {}
    for task, keywords in TASK_KEYWORDS.items():
        hits = sum(1 for kw in keywords if kw in query_lower)
        if hits > 0:
            scores[task] = hits
    if not scores:
        return "General / Unspecified"
    return max(scores, key=scores.get)


def detect_domain(query: str) -> str:
    query_lower = query.lower()
    scores = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        hits = sum(1 for kw in keywords if kw in query_lower)
        if hits > 0:
            scores[domain] = hits
    if not scores:
        return "General"
    return max(scores, key=scores.get)


def extract_keywords(query: str, max_keywords: int = 6) -> list:
    stopwords = {
        "i", "want", "to", "build", "a", "an", "the", "for", "of", "and", "that",
        "using", "with", "is", "in", "on", "system", "model", "project", "my",
        "app", "application",
    }
    words = re.findall(r"[a-zA-Z]+", query.lower())
    keywords = [w for w in words if w not in stopwords and len(w) > 2]
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