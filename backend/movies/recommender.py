# backend/recommender.py
import json
import random

# Load movies from JSON
with open("movies_dataset.json", "r", encoding="utf-8") as f:
    MOVIES = json.load(f)

# Mapping from emotion to genres
EMOTION_GENRE_MAP = {
    "happy": ["Comedy", "Family", "Animation", "Adventure"],
    "sad": ["Drama", "Romance"],
    "angry": ["Action", "Crime", "Thriller"],
    "relaxed": ["Documentary", "Fantasy", "Music"],
    "bored": ["Sci-Fi", "Mystery", "Adventure"],
    "romantic": ["Romance", "Drama", "Music"],
    "excited": ["Action", "Adventure", "Thriller"],
}


def recommend_movies_by_emotion(emotion: str, top_k: int = 5):
    genres = EMOTION_GENRE_MAP.get(emotion.lower())
    if not genres:
        return {"error": "Unsupported emotion"}

    matching_movies = [
        movie for movie in MOVIES
        if any(genre in movie.get("genres", []) for genre in genres)
    ]

    if not matching_movies:
        return {"error": "No movies found for this emotion"}

    return random.sample(matching_movies, min(top_k, len(matching_movies)))