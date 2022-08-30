from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Question
from django.contrib import messages

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    posts = {
            'posts' : latest_question_list,
        }
    
    print(posts)
    return render(request, 'home.html', posts)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    # Shortcut
    question = get_object_or_404(Question, pk=question_id)
    posts = {
            'posts' : question,
        }
    return render(request, 'detail.html', posts)


def results(request, question_id):
    return HttpResponse(f"You are looking at results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")


