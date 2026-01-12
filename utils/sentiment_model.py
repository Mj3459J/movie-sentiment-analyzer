import pickle
import numpy as np # type: ignore

# Load trained TF-IDF vectorizer
with open("tfidf_vectorizer.pkl","rb") as f:
    vectorizer=pickle.load(f)

# Load traied LR model
with open("lr_model.pkl","rb") as f:
    model=pickle.load(f)

def analyze_reviews(reviews):
    if len(reviews)==0:
        return None,0,0,"No reviews available"
    # Convert text to numerical form
    X=vectorizer.transform(reviews)

    # Predict Sentiment
    prediction=model.predict(X)  # 0 or 1
    probalities=model.predict_proba(X) # confidence

    # Day 6 logic for rating
    positive_count=int(prediction.sum())
    negative_count=len(prediction)-positive_count

    avg_positive_prob=probalities[:,1].mean()
    rating=round(avg_positive_prob*10,1)

    recommendation=(
        "Recommended to watch" if rating>=6
        else "Not Recommended to watch"
    )

    return rating,positive_count,negative_count,recommendation