from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest, JsonResponse
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
        print(bodyreq)
        return JsonResponse(bodyreq, safe=False, json_dumps_params={'ensure_ascii':False})
    except Exception as e:
        print(e)

@require_POST
def choice(request: HttpRequest):
    try:
        bodyreq = json.loads(request.body.decode('utf-8'))
        question = models.Question.objects.get(id=bodyreq['question_id'])
        models.Choice.objects.create(question=  question, choice_text=bodyreq['choice_text'])
        return JsonResponse(bodyreq,safe=False,json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)


# require get dos outros dados
