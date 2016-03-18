from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from .models import Story



class IndexView(generic.ListView):
    template_name = 'iamgrey/story_list.html'
    context_object_name = 'latest_story_list'
    latest_story = Story.objects.latest('date_published')

    def get_queryset(self):
        """Return the last five published questions."""
        return Story.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['latest_story'] = Story.objects.latest('date_published')
        return context     
    
class DetailView(generic.DetailView):
    model = Story
    template_name = 'iamgrey/detail.html'