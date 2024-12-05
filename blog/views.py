from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest):
    try:
        bodyreq = request.body
        return HttpResponse(bodyreq)
    except:
        ...