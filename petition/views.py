from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.template import RequestContext
from .models import Petition
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

	
class PetitionView(generic.ListView):
	template_name = 'petition/petition.html'
	context_object_name = 'latest_petition_list'

	def get_queryset(self):
		return Petition.objects.all()[:1]


def vote(request, petition_id):
	p = get_object_or_404(Petition, pk=petition_id)
	try:
		selected_vote = p.vote_set.get(pk=request.POST['vote'])
	except (KeyError, Vote.DoesNotExist):
		return render(request, 'petition/petition.html'), {
		'petition' : p, 
		'error_message' : "you didn't support the petition"
		}
	else:
		selected_vote.votes  += 1
		selected_vote.save()
 		return HttpResponseRedirect(reverse('petition:petition'))
