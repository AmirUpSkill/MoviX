from sqlalchemy import Column, Integer, String, Date, ARRAY, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Movie(Base):
    """
    SQLAlchemy ORM model for the movies table.
    
    Maps to the database schema created by our ingest.py script.
    Supports async operations via AsyncSession.
    """
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    overview = Column(Text, default="")
    genres = Column(ARRAY(String), nullable=False)
    cast = Column(ARRAY(String), nullable=False)
    director = Column(ARRAY(String), nullable=False)
    poster_url = Column(String)
    release_date = Column(Date)

    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}', release_date={self.release_date})>"
