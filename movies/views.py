# from asyncio.windows_events import NULL
from doctest import debug_script
from os import link
# from flask import Flask,render_template,request
from django.http import HttpResponse
from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np
import requests
# from home.forms import HomeForm

# app=Flask(__name__)

# @app.route('/')
def homepage(request):
    return render(request,'home_page.htm')

#########################################################################


def holly_fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=58031aee55d1dd21da825c4dc83935ce&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def holly_recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    # movie_index=285
    # print(movies_list['title']==movie)
    # print(movies_list['title']==movie)
    distances=similarity[movie_index]
    movies_list1=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list1:
        movie_id=movies.iloc[i[0]].movie_id#for poster
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(holly_fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters



movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
# print(movies['title'])
movies_list=movies_list['title'].values 
similarity=pickle.load(open('similarity.pkl','rb'))




# @app.route('/hollywood')
def hollywood(request):
    return render(request,'hollywood.htm')



# @app.route('/holly_predict',methods=['POST'])

def holly_predict(request):

    holly_selected_movie_name="Avtar"
    # for x in request.form.values():
        # print(x)
        # holly_selected_movie_name=x
        # break
    print(holly_selected_movie_name)
    print(request.POST)
    holly_selected_movie_name=request.POST.get ('holly_movie_name')
    print(holly_selected_movie_name)
    names,posters=holly_recommend(holly_selected_movie_name)
    args={
    'holly_selected_movie_name':holly_selected_movie_name,
    'holly0':names[0],
    'poster0':posters[0],
    'holly1':names[1],
    'poster1':posters[1],
    'holly2':names[2],
    'poster2':posters[2],
    'holly3':names[3],
    'poster3':posters[3],
    'holly4':names[4],
    'poster4':posters[4]
    }
    return render(request,'holly_predict.htm',args)




# ############################################################################

def bolly_fetch_poster(bolly_movie_id):
    return bolly_poster_dict[bolly_movie_id]

def bolly_fetch_link(bolly_movie_id):
    return bolly_wiki_dict[bolly_movie_id]


def recommend_bolly(movie): 
    bolly_movie_index=bolly_movies[bolly_movies['original_title'] == movie].index[0]
    print(bolly_movie_index)
    # movie_index=285
    # print(movies_list['title']==movie)
    # print(movies_list['title']==movie)
    distances=bolly_similarity[bolly_movie_index]
    bolly_movies_list1=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    bolly_recommended_movies=[]
    bolly_recommended_movies_posters=[]
    bolly_link=[]
    for i in bolly_movies_list1:
        bolly_movie_id=bolly_movies.iloc[i[0]].imdb_id#for poster
        bolly_recommended_movies.append(bolly_movies.iloc[i[0]].original_title)
        bolly_recommended_movies_posters.append(bolly_fetch_poster(bolly_movie_id))
        bolly_link.append(bolly_fetch_link(bolly_movie_id))
    return bolly_recommended_movies,bolly_recommended_movies_posters,bolly_link


bolly_movies_list=pickle.load(open('bolly_movies.pkl','rb'))
bolly_movies=pd.DataFrame(bolly_movies_list)
# print(movies['title'])
bolly_movies_list=bolly_movies_list['original_title'].values 
bolly_similarity=pickle.load(open('bolly_similarity.pkl','rb'))
bolly_poster_dict=pickle.load(open('bolly_poster_dict.pkl','rb'))
bolly_wiki_dict=pickle.load(open('bolly_wiki_dict.pkl','rb'))

# @app.route('/')
# def hollywood():
#     return render_template('hollywood.htm')

# @app.route('/bollywood')
def bollywood(request):
    return render(request,'bollywood.htm')


# @app.route('/bolly_predict',methods=['POST'])
def bolly_predict(request):

    bolly_selected_movie_name=request.POST.get('bolly_movie_name')
    # for x in request.form.values():
    #     print(x)
    #     bolly_selected_movie_name=x
        # break
    names,posters,link=recommend_bolly(bolly_selected_movie_name)
    args={
        'bolly_selected_movie_name':bolly_selected_movie_name,
        'bolly0':names[0],
        'poster0':posters[0],
        'link0':link[0],
        'link1':link[1],
        'link2':link[2],
        'link3':link[3],
        'link4':link[4],
        'bolly1':names[1],
        'poster1':posters[1],
        'bolly2':names[2],
        'poster2':posters[2],
        'bolly3':names[3],
        'poster3':posters[3],
        'bolly4':names[4],
        'poster4':posters[4]
    }

    return render(request,'bolly_predict.htm',args)
    # col1,col2,col3,col4,col5=st.columns(5)
    
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])

    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])

    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])

    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])

    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])


# if(__name__=="__main__"):
#     app.run(debug=True)