from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_POST

@require_POST
def index(request: HttpRequest):
    try:
        bodyreq = request.body
        return HttpResponse(bodyreq)
    except:
        ...
        
@require_POST
def cadastro_paciente(request: HttpRequest):
    try:
        bodyreq = request.body
        return HttpResponse(bodyreq)
    except:
        ...

@require_POST        
def cadastro_endereco(request: HttpRequest):
    try:
        bodyreq = request.body
        return HttpResponse(bodyreq)
    except:
        ...

@require_POST        
def cadastro_clinica(request: HttpRequest):
    try:
        bodyreq = request.body
        return HttpResponse(bodyreq)
    except:
        ...

@require_POST        
def cadastro_profissional(request: HttpRequest):
    try:
        bodyreq = request.body
        return HttpResponse(bodyreq)
    except:
        ...