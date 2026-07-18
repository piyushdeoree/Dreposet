from app.services.intent_parser import parse_intent

if __name__ == "__main__":
    queries = [
        "I want to build a fake news detection model",
        "Predict loan defaults for a bank",
        "Build a recommendation system for e-commerce products",
        "Detect objects in traffic camera images",
    ]

    for q in queries:
        result = parse_intent(q)
        print(f"\nQuery: {q}")
        print(f"  Task:     {result['task']}")
        print(f"  Domain:   {result['domain']}")
        print(f"  Keywords: {result['keywords']}")