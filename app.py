import streamlit as st
from utils.movie_search import search_movie
from utils.review_fetcher import fetch_reviews
from utils.sentiment_model import analyze_reviews

# Session state:

# Has the user clicked a movie title?
if "movie_selected" not in st.session_state:
    st.session_state.movie_selected=False

# Which movie was clicked
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie=None

# Has the user searched something?
if "searched" not in st.session_state:
    st.session_state.searched=False

# Stores Previous movie name and Used to reset sentiment when a new movie is searched
if "last_search" not in st.session_state:
    st.session_state.last_search=""


st.title("Movie Sentiment Analyzer")
st.write("Decide a movie is worth watching.")

movie_name=st.text_input("Search movie")
if st.button("Search"):
    if movie_name:
        # RESET old state when new search happens
        if movie_name!=st.session_state.last_search:
            st.session_state.movie_selected=False
            st.session_state.selected_movie=None
        
        st.session_state.searched=True
        st.session_state.last_search=movie_name
    else:
        st.warning("Please enter a movie name")

if st.session_state.searched and movie_name:
    st.write(f"Showing results for **{movie_name}**")

    movies = search_movie(movie_name)

    if movies:
        movie = movies[0]

        poster_url = "https://image.tmdb.org/t/p/w500" + movie["poster_path"]
        st.image(poster_url, width=180)

        if st.button(movie["title"]):
            st.session_state.movie_selected=True
            st.session_state.selected_movie=movie

        st.write("Click the Title of movie to perform Sentiment Analysis")

    else:
        st.warning("No movie found.")

if  st.session_state.selected_movie and st.session_state.movie_selected:
    st.subheader("Sentiment Analysis result:")
    st.info("Analyzing audience sentiment based on reviews...")
    # Day 9 logic.
    movie=st.session_state.selected_movie
    movie_id=movie["id"]

    # Fetch reviews
    reviews=fetch_reviews(movie_id)

    # Analyze reviews using ML model
    rating,pos,neg,recommendation=analyze_reviews(reviews)

    # Display output safely
    if rating is None:
        st.warning("Not enough public reviews available for analysis")
    else:
        st.write(f"Rating: {rating}")
        st.write(f"Positive reviews: {pos}")
        st.write(f"Negative reviews: {neg}")
        st.success(recommendation)
    