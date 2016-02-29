from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from .models import Post


# Create your views here.

# def post_list(request):
# 	posts = Post.objects.filter(date_published__lte=timezone.now()).order_by('date_published')

# 	return render(request, 'blog/post_list.html', {'posts': posts})

class IndexView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.filter(date_published__lte=timezone.now())


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'