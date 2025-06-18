# 🎬 Movie Recommender App

An interactive movie recommendation system built with Python and Streamlit.  
It recommends similar movies based on a selected title using content-based filtering.

## 🔧 Features
- Select a movie and get 5 similar recommendations
- Uses TMDB 5000 dataset (movies + credits)
- Streamlit frontend
- Cosine similarity on TF-IDF vectors

## 📦 Tech Stack
- Python
- Streamlit
- scikit-learn
- pandas
- TMDB API (for poster fetching)

## 🚀 How to Run Locally

```bash
git clone https://github.com/Karthik31Reddy/movie_recommender.git
cd movie_recommender
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
streamlit run app.py
