import streamlit as st
from recommender import load_data, build_similarity_matrix, recommend

st.title("🎬 Movie Recommendation App")

movies = load_data()
similarity_matrix = build_similarity_matrix(movies)

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie you like:", movie_list)

if st.button("Get Recommendations"):
    results = recommend(selected_movie, movies, similarity_matrix)
    for i, row in results.iterrows():
        st.subheader(row['title'])
        st.write(row['overview'])  # showing the correct column
        # st.write(movies.columns)

        # st.write(f"Genres: {row['genres']}")
        # st.write(f"Cast: {row['cast']}")
        # st.write(f"Crew: {row['crew']}")