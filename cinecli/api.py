# cinecli/api.py

import requests

BASE_URL = "https://yts.lt/api/v2"

def search_movies(query: str, limit: int = 10):
    params = {
        "query_term": query,
        "limit": limit,
    }
    response = requests.get(f"{BASE_URL}/list_movies.json", params=params, timeout=10)
    response.raise_for_status()
    return response.json()["data"].get("movies", [])

def get_movie_details(movie_id: int):
    params = {
        "movie_id": movie_id,
        "with_images": True,
        "with_cast": True,
    }
    response = requests.get(f"{BASE_URL}/movie_details.json", params=params, timeout=10)
    response.raise_for_status()
    return response.json()["data"]["movie"]
