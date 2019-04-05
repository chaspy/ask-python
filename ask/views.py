from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Question, Message
# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

class IndexView(generic.ListView):
    template_name = 'ask/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return all questions."""
        return Question.objects.order_by('user_id')[:]
