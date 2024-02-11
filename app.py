



import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=04204329e1e967dc9d7fc0085c0dfd11'.format(id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0] #here we are trying to search for a movie given by user say 'avatar'
  distances=similar[movie_index] #IF THE MOVIE WE ARE SEARCHING IS AVATAR then we extract its similarity score with all other 4000 words
  movies_list= sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:7]
  recommend_movies=[]
  recommended_movies_poster=[]
  for i in movies_list:
    movie_id = movies.iloc[i[0]].id_x
    #fetch poster, login to imdb data find a api key and a get rewuest through id check dcumentation anfd get url, in that api call a json is retured

    recommend_movies.append(movies.iloc[i[0]].title)
    recommended_movies_poster.append(fetch_poster(movie_id))
  return recommend_movies, recommended_movies_poster

st.title('MOVIES RECOMMENDATION!')
#convert the dataframe to dictionary and pass to pickle
# Fetch large pickle file from Google Drive
#file_url = "https://drive.google.com/file/d/1Ob9MJ6zkwA_K5dnUNuhBeixEwW5ZvLSe"
# def download_file_from_google_drive(file_id, destination):
#     url = f'https://drive.google.com/uc?id={file_id}'
#     response = requests.get(url)
#     with open(destination, 'wb') as f:
#         f.write(response.content)

# Replace 'your_file_id' and 'destination_path' with the actual values
# file_id = '1Ob9MJ6zkwA_K5dnUNuhBeixEwW5ZvLSe'
# destination_path = 'destination_path.pkl'
#
# download_file_from_google_drive(file_id, destination_path)
#
# similar = pickle.load(open(destination_path, 'rb'))



similar = pickle.load(open('similarity.pkl', 'rb'))
movie_list = pickle.load(open('movies.pkl', 'rb')) #opening the datafram we stored in pickle file in read binary mode
movies = pd.DataFrame(movie_list)


option = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend:)'):
    rec, posters=recommend(option)

    # for i in rec:
    #     st.write(i) #We cann add movie poster using id no

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 =st.columns(3)

    with col1:
        st.text(rec[0])
        st.image(posters[0])
    with col2:
        st.text(rec[1])
        st.image(posters[1])
    with col3:
        st.text(rec[2])
        st.image(posters[2])
    with col4:
        st.text(rec[3])
        st.image(posters[3])
    with col5:
        st.text(rec[4])
        st.image(posters[4])
    with col6:
        st.text(rec[5])
        st.image(posters[5])






#retrieving the list of movies from google collab
#added a pickle file of the movie_final dataframe
