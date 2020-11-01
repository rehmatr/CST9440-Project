#Program by Tejus Revi
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context
import pymongo


listOfMovies = []
PASSWORD = "team20"
DATABASE_NAME = "testDB"
myclient = pymongo.MongoClient("mongodb+srv://tejus:"+PASSWORD+"@cluster0.ymzum.gcp.mongodb.net/"+DATABASE_NAME+"?retryWrites=true&w=majority")
mydb = myclient["test"]
mycol = mydb["testCollection"]

#cursorOfMovies is a cursor object that stores all movies from DB
cursorOfMovies = mycol.find()

for movie in cursorOfMovies:
    listOfMovies.append(movie)

def View(request):
    context = {"listOfMovies":listOfMovies}
    response = render(request, 'index.html', context)
    return response

def navigate_to_movie(request):
    imdbid = request.GET.get('key', '')
    movie = mycol.find_one({ "imdbID": imdbid })
    context = {"movie":movie}
    response = render(request, 'movie.html', context)

    return response
def view_database(request):
    context = {"listOfMovies":listOfMovies}
    response = render(request, 'database.html', context)
    return response
