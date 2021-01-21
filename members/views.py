from django.http.response import HttpResponse
from django.shortcuts import redirect, render


from .models import Question
from django.db.models import Q

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'members/index.html', context)

def index_s(request):
    latest_question_list = Question.objects.order_by('-pub_date')[1:5] #a:b a+1부터 b까지 , :5 처음부터4까지 
    #qs = Question.objects.get(id=4)
    # get() 은 하나만 가져온다.
    qs = Question.objects.filter(Q(question_text__startswith='Wha') | Q(question_text__startswith='duru'))
    #https://docs.djangoproject.com/en/3.1/topics/db/queries/ d
    output = ', '.join([q.question_text for q in latest_question_list]) #list_comprehense
    return HttpResponse(','.join([q.question_text for q in qs]))


def get_index(req):
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