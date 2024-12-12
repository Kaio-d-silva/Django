from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_POST
from models import Choice, Question


@require_POST
def index(request: HttpRequest):
    try:
        bodyreq = request.body
        return HttpResponse(bodyreq)
    except:
        ...
        
@require_POST
def question(request: HttpRequest):
    try:
        bodyreq = request.body
        Question.objects.create(question_class='', pub_date='')
        return HttpResponse(bodyreq)
    except:
        ...
        
  
  
  
        
@require_POST
def choice(request: HttpRequest):
    try:
        bodyreq = request.body
        Choice.objects.create(question='',choice_texte='',votes='')
        return HttpResponse(bodyreq)
    except:
        ...