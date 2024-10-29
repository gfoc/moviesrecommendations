import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=1926c0b23da3b51a7faba85ac2465c24&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')

st.title("Write your favourite movie name")


def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distance = similarity_[movie_index]
        movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []
        for i in movie_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))

        return recommended_movies, recommended_movies_posters
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return [], []


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity_ = pickle.load(open('similarity.pkl', 'rb'))

option = st.selectbox("Select any movie", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(option)
    if names and posters:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.text(names[idx])
                st.image(posters[idx])
    else:
        st.write("No recommendations available.")
