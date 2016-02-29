from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static, serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$',  views.IndexView.as_view(), name='post_list'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

   
   
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
