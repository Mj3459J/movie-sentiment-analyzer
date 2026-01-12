# Movie Sentiment Analyzer

A machine learning web application that analyzes movie reviews and generates Rating based on the reviews to help users decide whether a movie is worth watching.

## Features
- Search movies using TMDB API
- Display movie posters and details
- Fetch real user reviews
- Sentiment analysis using Logistic Regression
- Rating generation based on reviews
- Recommendation based on sentiment score

## Machine Learning
- Dataset: IMDb 50K Movie Reviews
- Text Representation: TF-IDF
- Model: Logistic Regression
- Output: Rating (0–10) + Recommendation

## Tech Stack
- Python
- Scikit-learn
- Streamlit
- TMDB API
- Pandas, NumPy

## How to Run
```bash
conda activate movie-sentiment-ml
streamlit run app.py
