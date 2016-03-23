from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Question

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now())

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choise = p.choise_set.get(pk=request.POST['choise'])
    except (KeyError, Choise.DoesNotExist):
        # Redisplay the question voting form.
        
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choise.",
        })
    else:
        selected_choise.votes += 1
        selected_choise.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:index'))
