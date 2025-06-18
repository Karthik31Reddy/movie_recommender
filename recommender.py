import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    # Load both datasets
    movies = pd.read_csv("data/movies.csv")
    credits = pd.read_csv("data/tmdb_5000_credits.csv")

    # Merge on movie ID
    merged = movies.merge(credits, left_on='id', right_on='movie_id')

    # We'll keep only the columns we need
    merged = merged[['title_x', 'overview', 'genres', 'cast', 'crew']]
    merged = merged.rename(columns={'title_x': 'title'})

    return merged


def build_similarity_matrix(movies):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['overview'].fillna(''))
    return cosine_similarity(tfidf_matrix)

def recommend(movie_title, movies, similarity_matrix):
    idx = movies[movies['title'] == movie_title].index[0]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in scores[1:6]]
    return movies.iloc[top_indices]

