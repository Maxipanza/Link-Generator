from re import template
from select import select
from typing_extensions import Self
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote_http(request, question_id):
    try:
        choice_id = request.POST['choice']
        vote(question_id, choice_id)
    except(KeyError, Question.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question_id,
            'error_message': "Pregunta incorrecta",
            })
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question_id,
            'error_message': "No seleccionaste una choice",
            })
    else:
        #selected_choice.votes += 1
        question = Question.objects.get(pk=question_id)
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
        
def vote(question_id, choice_id):
    question = Question.objects.get(pk=question_id)
    selected_choice = question.choice_set.get(pk=choice_id)
    selected_choice.votes += 1
    selected_choice.save()

def vote_commandline():
    question_id = None  #leer de la linea de comando
    choice_id = None  #leer de la linea de comando
    vote(question_id, choice_id)
    print("algopiolaparaelusuario")
