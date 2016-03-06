from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views import generic
from .models import Event


class AgendaView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'latest_event_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Event.objects.filter(date_event__gte=timezone.now())

def verhalen(request): 
    return render(request , 'home/verhalen.html')

def aboutus(request):
    return render(request , 'home/aboutus.html')