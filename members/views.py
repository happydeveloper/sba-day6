from django.http.response import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.

def index(req):
    # url?id=duru 로 접속했을 경우
    #id = req.GET.get('id', '') #id querystring id 값이 비어서 들어올경우 에러가 나지 않도록 조치
    id = req.GET['id']
    if (req.method == 'GET' and id == 'duru'):
        return redirect('/home')

    return HttpResponse("<h1>hello world</h1>"+id)



def detail(request, question_id):
    return HttpResponse(f"You're {question_id} looking at question {question_id} ")

def results(request, question_id):
    response = "You're looking at the results of question %s %s."
    return HttpResponse(response % (question_id, question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)