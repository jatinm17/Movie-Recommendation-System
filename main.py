import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=594792ed6bfe522d746bef0c479790c7&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommend_movies_posters=[]
    for i in movie_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies,recommend_movies_posters

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name=st.selectbox('What you will like to watch?',movies['title'].values)
if st.button('Show Recommendation'):
    recommended_movies,recommend_movies_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommend_movies_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommend_movies_posters[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommend_movies_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommend_movies_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommend_movies_posters[4])