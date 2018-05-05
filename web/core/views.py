from django.shortcuts import render, HttpResponse, render_to_response
from django.http import JsonResponse
from leaflet.forms.widgets import LeafletWidget
import json
import requests 


j = requests.get('https://s3-us-west-2.amazonaws.com/lgoveabucket/data_melp.json')

js = j.json() 

# Create your views here.
def home (request):
    return render (request, "core/home.html")

def show_all (request):
    return render_to_response('core/show_all.html', {'list':js})

def map (request):

    return render (request,"core/map.html",{'list': js})