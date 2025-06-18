import streamlit as st
from recommender import load_data, build_similarity_matrix, recommend
from huggingface_assistant import query_huggingface_model
st.title("🎬 Movie Recommendation App")

movies = load_data()
similarity_matrix = build_similarity_matrix(movies)

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie you like:", movie_list)

if st.button("Get Recommendations"):
    results = recommend(selected_movie, movies, similarity_matrix)
    for i, row in results.iterrows():
        st.subheader(row['title'])
        st.write(row['overview']) 
        import streamlit as st


st.header("💬 Ask the AI Assistant")
user_input = st.text_input("Ask me something about movies:")

if st.button("Ask"):
    if user_input:
        result = query_huggingface_model(user_input)
        st.write("🤖", result)
    else:
        st.warning("Please type something first.")
