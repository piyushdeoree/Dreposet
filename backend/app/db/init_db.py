from app.db.database import Base, engine
from app.db import models  # noqa: F401  (import so models register with Base)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")

if __name__ == "__main__":
    init_db()