import streamlit as st
import pandas as pd
import pickle
from streamlit_lottie import st_lottie_spinner
import requests
from PIL import Image
import time

img= Image.open("headerlogo.png")
st.set_page_config(page_title='MuviEra',layout="wide", page_icon=img)

hide_st_style = """
            <style>
            #MainMenu {visibility: visible;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #d85f25;">
  <a class="navbar-brand" href="http://127.0.0.1:8000" target="_blank"></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="http://127.0.0.1:8000/recommendation/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/ronitttm/muviera-movie/main/movie.py" target="_blank">Movie</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://127.0.0.1:8000/feedback/" target="_blank">Feedback</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

def loadgifs(url : str ):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_wait_url= "https://assets9.lottiefiles.com/packages/lf20_f1qtk0oe.json"
lottie_wait = loadgifs(lottie_wait_url)

def recommend(music):
    music_index= music_data[music_data['title']==music].index[0]
    distances= similarity[music_index]
    music_list = sorted(list(enumerate(distances)),reverse=True,key= lambda x:x[1])[1:19]

    recommended_music = []
    for i in music_list:
        recommended_music.append(music_data.iloc[i[0]].title)
    return recommended_music

music_dict = pickle.load(open('music.pkl', 'rb'))
music_data = pd.DataFrame(music_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('MuviEra-A Recommendation System')
music_list  = music_data['title'].values
selected_music = st.selectbox(
"Type or select a movie from the dropdown",
music_list
)

st.write('You selected:', selected_music)


if st.button('Show Recommendation'):
    with st_lottie_spinner(lottie_wait, key='wait'):
        time.sleep(4)
    recommendations = recommend(selected_music)
    col1, col2, col3, col4, col5 , col6, col7, col8= st.columns(8)
    with col1:
        st.text(recommendations[0])
        st.image('musiclogo.png')
    with col2:
        st.text(recommendations[1])
        st.image('musiclogo.png')

    with col3:
        st.text(recommendations[2])
        st.image('musiclogo.png')
    with col4:
        st.text(recommendations[3])
        st.image('musiclogo.png')
    with col5:
        st.text(recommendations[4])
        st.image('musiclogo.png')
    with col6:
        st.text(recommendations[5])
        st.image('musiclogo.png')
    with col7:
        st.text(recommendations[6])
        st.image('musiclogo.png')
    with col8:
        st.text(recommendations[7])
        st.image('musiclogo.png')

if st.button('Next'):
    with st_lottie_spinner(lottie_wait, key='wait'):
        time.sleep(4)
    recommendations = recommend(selected_music)
    col1, col2, col3, col4, col5 , col6, col7, col8= st.columns(8)
    with col1:
        st.text(recommendations[8])
        st.image('musiclogo.png')
    with col2:
        st.text(recommendations[9])
        st.image('musiclogo.png')

    with col3:
        st.text(recommendations[10])
        st.image('musiclogo.png')
    with col4:
        st.text(recommendations[11])
        st.image('musiclogo.png')
    with col5:
        st.text(recommendations[12])
        st.image('musiclogo.png')
    with col6:
        st.text(recommendations[13])
        st.image('musiclogo.png')
    with col7:
        st.text(recommendations[14])
        st.image('musiclogo.png')
    with col8:
        st.text(recommendations[15])
        st.image('musiclogo.png')
