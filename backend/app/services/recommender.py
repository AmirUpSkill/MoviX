from __future__ import annotations 

import joblib 
import numpy as np 
import pandas as pd
from pathlib import Path 
from typing import List , Optional 
import scipy.sparse as sp 

from app.schemas.movie import Movie 

MODEL_DIR = Path(__file__).resolve().parent.parent.parent / "models"

class RecommendationService:
    """
        Singleton-like service that loads artifacts once and serves recommendations . 
    """
    _instance: Optional["RecommendationService"] = None 
    _loaded = False 

    def __new__(cls) -> "RecommendationService":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if self._loaded:
            return
        print("[INFO] Loading ML artifacts...")
        self.vectorizer: "TfidfVectorizer" = joblib.load(MODEL_DIR / "tfidf_vectorizer.joblib")
        self.tfidf_matrix: sp.csr_matrix = sp.load_npz(MODEL_DIR / "tfidf_matrix.npz")
        self.movies_meta: pd.DataFrame = pd.read_parquet(MODEL_DIR / "movies_meta.parquet")
        self._loaded = True
        print("[INFO] Artifacts loaded.")
    # --- Public Api --- 
    def get_recommendations(
        self,
        genres: Optional[List[str]] = None , 
        actors: Optional[List[str]] = None,
        keywords: Optional[List[str]] = None , 
        k: int = 5,
    ) -> List[Movie]:
        """
            Return up to "k" top-matching movies . 
        """
        query_tokens = self._build_query_tokens(genres , actors , keywords)

        if not query_tokens:
            return []
        q_vec = self.vectorizer.transform([" ".join(query_tokens)])
        scores = (self.tfidf_matrix @ q_vec.T).toarray().ravel()

        # --- Pic top-k indices ---
        top_k = min(k , len(scores))
        top_idx = np.argpartition(-scores, top_k - 1)[:top_k]
        top_idx = top_idx[np.argsort(-scores[top_idx])]

        matched_df = self.movies_meta.iloc[top_idx].drop_duplicates(subset=["id"])
        return [Movie(**row) for row in matched_df.to_dict(orient="records")]
    # --- HELPER Function ---
    @staticmethod
    def _build_query_tokens(
        genres: Optional[List[str]],
        actors: Optional[List[str]],
        keywords: Optional[List[str]],
    ) -> List[str]:
        tokens = []
        tokens += [f"genre={g}" for g in (genres or [])]
        tokens += [f"actor={a}" for a in (actors or [])]
        tokens += keywords or []
        # up-weight structured tokens
        return tokens + tokens


