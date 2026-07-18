from sqlalchemy import Column, Integer, String, Text, JSON
from app.db.database import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    source = Column(String, nullable=False)
    description = Column(Text, default="")
    url = Column(String, nullable=False)
    domain = Column(String, default="")
    task = Column(String, default="")
    format = Column(String, default="")
    size = Column(String, default="")
    tags = Column(JSON, default=[])
    embedding = Column(JSON, default=None)   # NEW: stores the vector as a list of floats

class GitHubRepo(Base):
    __tablename__ = "github_repos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, default="")
    language = Column(String, default="Unknown")
    stars = Column(Integer, default=0)
    url = Column(String, nullable=False)
    topics = Column(JSON, default=[])
    embedding = Column(JSON, default=None)   # NEW