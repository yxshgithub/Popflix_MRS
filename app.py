from urllib import response
import streamlit as st
import pickle 
import requests

apikey = '8265bd1679663a7ea12ac168da84d2e8'

#features to display
finalresults_poster = []
finalresults_overview = []
finalresults_scores = []


def recommended(movie):
    Recom_list = [];
    index = moviesinfo[moviesinfo['original_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarities[index])),reverse=True,key = lambda x: x[1])

    finalresults = []
    for i in distances[1:6]:
        moviesidd = moviesinfo.iloc[i[0]].id
        finalresults.append(moviesinfo.iloc[i[0]].original_title)
        finalresults_poster.append(get_poster(moviesidd))
        finalresults_overview.append(get_overview(moviesidd))
        finalresults_scores.append(get_score(moviesidd))
    return finalresults
        

def get_poster(movieid):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movieid))
    data_bundle = response.json()
    return 'https://image.tmdb.org/t/p/w500' + data_bundle['poster_path']


def get_overview(movieid):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movieid))
    data_bundle = response.json()
    return data_bundle['overview']


def get_score(movieid):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movieid))
    data_bundle = response.json()
    return   data_bundle['vote_average']


moviesinfo = pickle.load(open('movies_list.pkl','rb'))
movieslist = moviesinfo['original_title'].values



# this is to fix the error during deployment (1st commit to resolve the issue)
# similarity = pickle.load(open('similarity.pkl','rb'))
similarities = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommendation System 🍿")
st.text("Pick a movie of your choice from 5000 movies given below")

movie_selected = st.selectbox(
    'Select a movie to get M.L.A Suggestions!',
    movieslist
)

clicked = st.button("Recommend me!!")
if clicked:
    st.write("Checkout the below Suggestions given")
    finalans = recommended(movie_selected)
    # for i in finalans:
    #     st.write(i)

    col1, col2, col3 , col4 , col5= st.columns(5)
    with col1:
        st.write(finalans[0])
        st.image(finalresults_poster[0])
        st.caption(finalresults_overview[0])
        st.text('⭐' + str(finalresults_scores[0])) 
    with col2:
        st.write(finalans[1])
        st.image(finalresults_poster[1])
        st.caption(finalresults_overview[1])
        st.text('⭐' + str(finalresults_scores[1])) 
    with col3:
        st.write(finalans[2])
        st.image(finalresults_poster[2])
        st.caption(finalresults_overview[2])
        st.text('⭐' + str(finalresults_scores[2])) 
    with col4:
        st.write(finalans[3])
        st.image(finalresults_poster[3])
        st.caption(finalresults_overview[3])
        st.text('⭐' + str(finalresults_scores[3])) 
    with col5:
        st.write(finalans[4])
        st.image(finalresults_poster[4])
        st.caption(finalresults_overview[4])
        st.text('⭐' + str(finalresults_scores[4])) 

    st.write("Made by Yash Sonawane! ")
    st.write("Github:- " + 'https://github.com/yxshgithub')
    st.write("Linkedin:- " + 'https://www.linkedin.com/in/yash-sonawane5621/')


st.text('© YASH SONAWANE')
