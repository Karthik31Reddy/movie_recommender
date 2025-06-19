
# # --- AI Assistant (Embedded from Hugging Face) ---
# st.header("💬 Ask CineBuddy (AI Assistant)")

# st.markdown("""
# <iframe 
#     src="https://huggingface.co/chat/assistant/6851992e5b2c3cbb5c223cf8" 
#     width="100%" 
#     height="600" 
#     style="border: 1px solid #ccc; border-radius: 8px;"
# ></iframe>
# """, unsafe_allow_html=True)
# # --- AI Assistant: Open in New Tab ---
# st.header("💬 Ask CineBuddy (AI Assistant)")

# st.write("Click below to chat with CineBuddy — your smart movie assistant!")

# assistant_url = "https://huggingface.co/chat/assistant/6851992e5b2c3cbb5c223cf8"
# st.markdown(f"""
#     <a href="{assistant_url}" target="_blank">
#         <button style='padding: 10px 20px; font-size: 16px;'>Open CineBuddy Chat 🚀</button>
#     </a>
# """, unsafe_allow_html=True)
import streamlit as st
from recommender import load_data, build_similarity_matrix, recommend

st.set_page_config(page_title="🎬 CineBuddy", page_icon="🎥")
st.title("🎬 Movie Recommendation App")

# Movie recommender
movies = load_data()
similarity_matrix = build_similarity_matrix(movies)

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie you like:", movie_list)

if st.button("Get Recommendations"):
    results = recommend(selected_movie, movies, similarity_matrix)
    for i, row in results.iterrows():
        st.subheader(row['title'])
        st.write(row['overview'])

# Hugging Face AI Assistant (open in new tab)
st.header("💬 Ask CineBuddy (AI Assistant)")
st.write("Click the button below to open CineBuddy — your smart movie assistant — in a new browser tab:")

assistant_url = "https://huggingface.co/chat/assistant/6851992e5b2c3cbb5c223cf8"

# Styled button link
st.markdown(f"""
    <a href="{assistant_url}" target="_blank">
        <button style='background-color:#4CAF50; color:white; padding:10px 20px; font-size:16px; border:none; border-radius:5px; cursor:pointer;'>
            Open CineBuddy Chat 🚀
        </button>
    </a>
""", unsafe_allow_html=True)
