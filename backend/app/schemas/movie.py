from pydantic import BaseModel, HttpUrl, Field
from datetime import date 
from typing import List, Optional

class MovieBase(BaseModel):
    """
    Base movie schema with core fields.
    Used for both input validation and response serialization.
    """
    id: int = Field(..., description="TMDB movie ID")
    title: str = Field(..., min_length=1, description="Movie title")
    release_date: date = Field(..., description="Movie release date")
    overview: str = Field(default="", description="Movie plot summary")
    poster_url: HttpUrl = Field(..., description="Full TMDB poster image URL")
    genres: List[str] = Field(..., min_length=1, description="Movie genres (normalized)")
    cast: List[str] = Field(..., min_length=1, description="Main cast members (max 5)")

class Movie(MovieBase):
    """
    Complete movie schema for API responses.
    Inherits all fields from MovieBase.
    """

    class Config:
        from_attributes = True 

# --- API Response Schemas --- 
class MoviesResponse(BaseModel):
    """
        Represents the paginated response from the GET/movies endpoint.

    """
    page: int 
    limit: int 
    total_movies: int 
    total_pages: int 
    data: List[Movie]

class RecommendationResponse(BaseModel):
    """
    Represents the response for the GET /recommendations endpoint.
    Returns exactly 5 movies as per API contract.
    """
    recommendations: List[Movie] = Field(..., max_length=5, description="Top 5 recommended movies")

# --- Request Validation Schemas ---
class RecommendationRequest(BaseModel):
    """
    Validates query parameters for recommendation requests.
    At least one filter must be provided.
    """
    genres: Optional[List[str]] = Field(None, description="Comma-separated genre names")
    actors: Optional[List[str]] = Field(None, description="Comma-separated actor names") 
    keywords: Optional[List[str]] = Field(None, description="Comma-separated keywords")
    
    def __init__(self, **data):
        super().__init__(**data)
        # Ensure at least one filter is provided
        if not any([self.genres, self.actors, self.keywords]):
            raise ValueError("Please provide at least one filter: genres, actors, or keywords")

class PaginationParams(BaseModel):
    """
    Standard pagination parameters for /movies endpoint.
    """
    page: int = Field(1, ge=1, description="Page number (starts at 1)")
    limit: int = Field(20, ge=1, le=100, description="Items per page (max 100)")
