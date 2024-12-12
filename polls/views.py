# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse, HttpRequest
# from django.views.decorators.http import require_POST

# @require_POST
# def index(request: HttpRequest):
#     try:
#         bodyreq = request.body
#         return HttpResponse(bodyreq)
#     except:
#         ...
        
# @require_POST
# def cadastro_paciente(request: HttpRequest):
#     try:
#         bodyreq = request.body
#         return HttpResponse(bodyreq)
#     except:
#         ...

# @require_POST        
# def cadastro_endereco(request: HttpRequest):
#     try:
#         bodyreq = request.body
#         return HttpResponse(bodyreq)
#     except:
#         ...

# @require_POST        
# def cadastro_clinica(request: HttpRequest):
#     try:
#         bodyreq = request.body
#         return HttpResponse(bodyreq)
#     except:
#         ...

# @require_POST        
# def cadastro_profissional(request: HttpRequest):
#     try:
#         bodyreq = request.body
#         return HttpResponse(bodyreq)
#     except:
#         ...


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_POST
from . import models
import json

@require_POST
def index(request: HttpRequest):
    try:
        body_unicode = request.body.decode('utf-8')
        bodyreq = json.loads(body_unicode)
        return HttpResponse(bodyreq)
    except Exception as e:
        ...
        
@require_POST
def question(request: HttpRequest):
    try:
        body_unicode = request.body.decode('utf-8')
        bodyreq = json.loads(body_unicode)
        models.Question.objects.create(question_class=bodyreq['question_class'], pub_date=bodyreq['pub_date'])
        return HttpResponse(bodyreq)
    except Exception as e:
        print(e)
        
  
  
  
        
@require_POST
def choice(request: HttpRequest):
    try:
        bodyreq = request.body
        models.Choice.objects.create(question='',choice_texte='',votes='')
        return HttpResponse(bodyreq)
    except:
        ...