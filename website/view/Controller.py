#Program by Tejus Revi
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context

def View(request):
    context = {}
    #Response provided to user
    response = render(request, 'index.html', context)
    return response
