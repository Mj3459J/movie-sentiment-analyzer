import requests

API_KEY="25400c916d47c0d01f592ad122c83993"
BASE_URL="https://api.themoviedb.org/3"

def search_movie(movie_name):
    url=f"{BASE_URL}/search/movie"

    params={
        "api_key":API_KEY,
        "query":movie_name
    }

    response=requests.get(url,params=params)
    data=response.json()

    return data["results"]