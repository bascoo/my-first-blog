from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static, serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$',  views.IndexView.as_view(), name='story_list'),
    # url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),   
      
   
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
