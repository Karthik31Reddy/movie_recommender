import requests
import os

API_KEY = os.getenv("3013dfaaa9655ccc306cacb6692e2448")  # or just hardcode for dev use

def fetch_poster(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
    response = requests.get(url).json()
    
    if response['results']:
        poster_path = response['results'][0].get('poster_path')
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_path
    return None
