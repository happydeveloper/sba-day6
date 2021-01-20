from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(req):
    return HttpResponse("<h1>hello world</h1>")

def str(request, question_str):
    return HttpResponse(f"You're {question_str} ")


def detail(request, question_id):
    return HttpResponse(f"You're {question_id} looking at question {question_id} ")

def results(request, question_id):
    response = "You're looking at the results of question %s %s."
    return HttpResponse(response % (question_id, question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)