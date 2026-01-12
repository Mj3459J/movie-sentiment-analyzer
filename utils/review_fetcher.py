import requests
import os

API_KEY=os.getenv("TMDB_API_KEY")
BASE_URL="https://api.themoviedb.org/3"

def fetch_reviews(movie_id,max_reviews=20):
    url=f"{BASE_URL}/movie/{movie_id}/reviews"
    params={
        "api_key":API_KEY,
        "language":"en-US"
    }

    response=requests.get(url,params=params)
    data=response.json()

    reviews=[]
    for r in data.get("results",[])[:max_reviews]:
        reviews.append(r["content"])
    # print("TMDB raw response:", data)
    
    return reviews