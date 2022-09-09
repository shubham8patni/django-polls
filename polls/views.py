from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, ChoiceForm, ChoiceInline
from django.forms import formset_factory
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     posts = {
#             'posts' : latest_question_list,
#         }
    
#     print(posts)
#     return render(request, 'home.html', posts)


class DetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'


# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")

#     # Shortcut
#     question = get_object_or_404(Question, pk=question_id)
#     posts = {
#             'posts' : question,
#         }
#     return render(request, 'detail.html', posts)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# def results(request, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'results.html', {'question' : question})
    


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        # question = {
        #     'question': question,
        #     'error_message': "You didn't select a choice.",
        # } 
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return render(request,'polls/index.html')
#             ...
#         else:
#             messages.error("wrong username or passsword!")
#             return render(request, 'polls/login.html')
#             ...
#     elif request.method == 'GET':
#         return render(request, 'polls/login.html')


@login_required
def new_poll(request):
    # form2 = formset_factory(ChoiceForm, extra=2)
    # formset = form2()
    if request.method == 'GET':
        form = QuestionForm()
        
        context = {'form' : form,}
        return render(request, 'polls/new_poll.html', {'form' : form}) # , 'form2' : formset, 
    
    elif request.method == 'POST':
        form = QuestionForm(request.POST) # , instance=request.user
        # form2 = form2(request.POST)
        # form3 = ChoiceForm(request.POST, instance=request.user)

        # print("222222222222222222222222222222222222",form.cleaned_data,form2.cleaned_data)
        if form.is_valid():
            print("222222222222222222222222222222222222",form)
            form.save()
            return redirect('polls:new-choices')
            # for i in form2:
            #     i.save()
            # form = form.cleaned_data
            # form2 = form2.cleaned_data
            # # form2['question'] = form['question_text']
            # for i in form2:
            #     i['question'] = form['question_text']
            # print("1111111111111111111111111111111111",form,form2)



@login_required
def new_choices(request):
    form2 = formset_factory(ChoiceForm, extra=2)
    formset = form2()
    if request.method == 'GET':
        return render(request, 'polls/new_choices.html', {'form' : formset})
    
    elif request.method == 'POST':
        form2 = form2(request.POST)
        
        # print("222222222222222222222222222222222222",form.cleaned_data,form2.cleaned_data)
        if form2.is_valid():
            print("222222222222222222222222222222222222",form2)
            # form.save()
            # return redirect('polls:index')

            # for i in form2:
            #     i.save()
            # form = form.cleaned_data
            # form2 = form2.cleaned_data
            # # form2['question'] = form['question_text']
            # for i in form2:
            #     i['question'] = form['question_text']
            # print("1111111111111111111111111111111111",form,form2)

       