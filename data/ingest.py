import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

load_dotenv() 

DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    raise RuntimeError("DATABASE_URL not found in .env")

POSTER_BASE = "https://image.tmdb.org/t/p/w500"

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """Return 300 clean rows."""
    # 1. Drop rows with nulls in required columns
    df = df.dropna(subset=["id", "title", "poster_path", "release_date"]).copy()

    # 2. Build poster_url
    df["poster_url"] = POSTER_BASE + df["poster_path"].astype(str)

    # 3. Normalize string-lists into arrays
    def to_arr(text, max_len=None):
        if not isinstance(text, str):
            return []
        tokens = [t.strip().lower().replace(" ", "-") for t in text.split(",") if t.strip()]
        return tokens[:max_len] if max_len else tokens

    df["genres"] = df["genres"].apply(lambda x: to_arr(x))
    df["cast"] = df["cast"].apply(lambda x: to_arr(x, 5))
    df["director"] = df["director"].apply(lambda x: to_arr(x, 1))

    # 4. Keep rows with non-empty arrays
    mask = df["genres"].str.len() > 0
    df = df[mask]

    # 5. Take top 300 by vote_count desc (or random)
    df = df.sort_values("vote_count", ascending=False).head(300)

    # 6. Final columns
    return df[["id", "title", "overview", "genres", "cast", "director", "poster_url", "release_date"]]

def upsert_to_db(clean: pd.DataFrame):
    """Upsert clean DataFrame into Neon."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS movies (
        id            integer PRIMARY KEY,
        title         text NOT NULL,
        overview      text,
        genres        text[] NOT NULL,
        "cast"        text[] NOT NULL,
        director      text[] NOT NULL,
        poster_url    text,
        release_date  date
    );
    """
    upsert_sql = """
    INSERT INTO movies (id, title, overview, genres, "cast", director, poster_url, release_date)
    VALUES %s
    ON CONFLICT (id) DO UPDATE
      SET title = EXCLUDED.title,
          overview = EXCLUDED.overview,
          genres = EXCLUDED.genres,
          "cast" = EXCLUDED."cast",
          director = EXCLUDED.director,
          poster_url = EXCLUDED.poster_url,
          release_date = EXCLUDED.release_date;
    """

    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute(create_table_sql)

    records = [
        (
            int(row.id),
            row.title,
            row.overview or "",
            row.genres,
            row.cast,
            row.director,
            row.poster_url,
            row.release_date,
        )
        for _, row in clean.iterrows()
    ]

    execute_values(cur, upsert_sql, records, template=None, page_size=1000)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    raw = pd.read_csv("data/TMDB_all_movies.csv")
    clean = clean_df(raw)
    upsert_to_db(clean)
    print(f"[INFO] {len(clean)} rows upserted into movies ✔")