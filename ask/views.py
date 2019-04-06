from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import redirect, get_object_or_404

from .models import Question, Message, User
# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

class IndexView(generic.ListView):
    template_name = 'ask/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return all questions."""
        return Question.objects.order_by('user_id')[:]


class QuestionView(generic.CreateView):
    """/question    question."""
    model = Question
    fields = ('question_text', )
    template_name = 'ask/question_form.html'
 
    def form_valid(self, form):
        user_id = self.request.session['_auth_user_id']
        question = form.save(commit=False)
        question.user_id = user_id
        question.status = False
        question.save()
 
        # redicrect top
        return redirect('/')

class DetailView(generic.CreateView):
    """/question    question."""
    model = Message
    fields = ('answer_text', )
    template_name = 'ask/detail.html'


    def get_context_data(self, **kwargs):
        question_pk = self.kwargs['pk']
        question = get_object_or_404(Question, pk=question_pk)
        context = super().get_context_data(**kwargs)
        context.update({
            'question': question
        })
        return context
 
    def form_valid(self, form):
        question_pk = self.kwargs['pk']
        question = get_object_or_404(Question, pk=question_pk)

        user_id = self.request.session['_auth_user_id']

        message = form.save(commit=False)
        message.user_id = user_id
        message.question = question
        message.save()
 
        # redicrect top
        # TODO redirect question  (I cannot change url pk=1)
        return redirect('/')