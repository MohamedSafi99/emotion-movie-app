# movies/views.py

import random
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

with open("movies_dataset.json", "r", encoding="utf-8") as f:
    MOVIES = json.load(f)

# Mood to genre mapping
MOOD_GENRE_MAP = {
    "Happy": ["Comedy", "Family"],
    "Sad": ["Comedy", "Drama"],
    "Excited": ["Action", "Adventure"],
    "Romantic": ["Romance"],
    "Bored": ["Action", "Thriller", "Sci-Fi"],
    "Adventurous": ["Adventure", "Fantasy"],
    "Angry": ["Action", "Thriller"],
    "Relaxed": ["Animation", "Family", "Fantasy"],
    "Lonely": ["Drama", "Romance"],
    "Nostalgic": ["Animation", "Family", "Drama"]
}

class SmartRecommendView(APIView):
    def post(self, request, *args, **kwargs):
        feeling = request.data.get("feeling", "")

        if feeling not in MOOD_GENRE_MAP:
            return Response({"detail": "Invalid mood selection."}, status=status.HTTP_400_BAD_REQUEST)

        genres = MOOD_GENRE_MAP[feeling]

        # Filter movies based on genre matching in overview (fallback logic)
        matched_movies = [movie for movie in MOVIES if any(genre.lower() in movie.get("overview", "").lower() for genre in genres)]

        if not matched_movies:
            matched_movies = random.sample(MOVIES, 5)

        selected_movie = random.choice(matched_movies)

        return Response(selected_movie)
