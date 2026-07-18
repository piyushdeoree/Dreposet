from sentence_transformers import SentenceTransformer

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")  # free, local, ~80MB download
    return _model

def embed_text(text: str):
    model = get_model()
    vector = model.encode(text, convert_to_numpy=True)
    return vector.tolist()  # JSON-serializable list of floats