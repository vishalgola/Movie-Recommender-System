import streamlit as st
import os
import pickle
import requests
import gdown


st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background-color: #0E1117;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #FF4B4B;
}
.subtitle {
    text-align: center;
    color: #AAAAAA;
    margin-bottom: 30px;
}
.movie-card {
    text-align: center;
}
.movie-title {
    font-size: 15px;
    font-weight: 600;
    margin-top: 8px;
}
.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<div class='title'>🎬 Movie Recommender</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Find movies you'll love in seconds</div>", unsafe_allow_html=True)


# ---------- LOAD DATA ----------
def download_file(file_id, filename):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, filename, quiet=False)

@st.cache_resource
def load_data():
    
    movie_url = "1eKCmH-a0qQNqdUVIdwJuZ5GzpzIkCi3x"
    similarity_url = "1kj3sKQqqYGpaarA10dVeVv-8IifGwP0V"

    # download only if not exists
    download_file(movie_url, "movie_list.pkl")
    download_file(similarity_url, "similarity.pkl")

    # load files
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    return movies, similarity

# # 🔥 Replace with your actual links
# movie_url = "https://drive.google.com/uc?id=1eKCmH-a0qQNqdUVIdwJuZ5GzpzIkCi3x"
# similarity_url = "https://drive.google.com/uc?id=1kj3sKQqqYGpaarA10dVeVv-8IifGwP0V"
#
# download_file(movie_url, "movie_list.pkl")
# download_file(similarity_url, "similarity.pkl")
# movies = pickle.load(open('movie_list.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------- SELECT ----------
movies, similarity = load_data()
movie_list = movies['title'].values
selected_movie = st.selectbox("🔍 Choose a movie", movie_list)


# ---------- FUNCTIONS ----------
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=9c74a2ced9cb1306e713c9eb05d87d92&language=en-US".format(
        movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    names = []
    posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        posters.append(fetch_poster(movie_id))
        names.append(movies.iloc[i[0]].title)

    return names, posters


# ---------- BUTTON ----------
if st.button("🚀 Recommend"):

    with st.spinner("Fetching best recommendations for you..."):
        names, posters = recommend(selected_movie)

    st.markdown("## 🔥 Recommended Movies")

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.image(posters[i], use_container_width=True)
            st.markdown(f"<div class='movie-title'>{names[i]}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<div class='footer'>Made with ❤️ using Streamlit | TMDB API</div>", unsafe_allow_html=True)
