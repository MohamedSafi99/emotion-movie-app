# backend/fetch_tmdb_movies.py
import requests
import json
import time

API_KEY = "e02a26043835a8ca314b224c24dc635a"
DISCOVER_URL = "https://api.themoviedb.org/3/discover/movie"
VIDEO_URL_TEMPLATE = "https://api.themoviedb.org/3/movie/{}/videos"
DETAILS_URL_TEMPLATE = "https://api.themoviedb.org/3/movie/{}"
BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

params = {
    "api_key": API_KEY,
    "language": "en-US",
    "sort_by": "popularity.desc",
    "include_adult": "false",
    "include_video": "false",
    "page": 1,
}

def fetch_trailer_url(movie_id):
    try:
        response = requests.get(
            VIDEO_URL_TEMPLATE.format(movie_id),
            params={"api_key": API_KEY}
        )
        videos = response.json().get("results", [])
        for video in videos:
            if video["type"] == "Trailer" and video["site"] == "YouTube":
                return f"https://www.youtube.com/watch?v={video['key']}"
    except:
        pass
    return None

def fetch_genres(movie_id):
    try:
        response = requests.get(
            DETAILS_URL_TEMPLATE.format(movie_id),
            params={"api_key": API_KEY}
        )
        genres = response.json().get("genres", [])
        return [genre["name"] for genre in genres]
    except:
        return []

def fetch_movies():
    all_movies = []
    for page in range(1, 300):  # Keep it 5 pages to avoid TMDB rate limits
        params["page"] = page
        response = requests.get(DISCOVER_URL, params=params)
        data = response.json()

        for movie in data.get("results", []):
            title = movie.get("title")
            overview = movie.get("overview")
            poster_path = movie.get("poster_path")
            movie_id = movie.get("id")

            if overview and len(overview) > 30 and poster_path:
                trailer_url = fetch_trailer_url(movie_id)
                genres = fetch_genres(movie_id)
                all_movies.append({
                    "title": title,
                    "overview": overview,
                    "poster_url": f"{BASE_IMAGE_URL}{poster_path}",
                    "trailer_url": trailer_url,
                    "genres": genres
                })
                time.sleep(0.3)  # Delay to avoid rate limiting

    with open("movies_dataset.json", "w", encoding="utf-8") as f:
        json.dump(all_movies, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved {len(all_movies)} movies with posters, trailers, and genres to movies_dataset.json")

if __name__ == "__main__":
    fetch_movies()
