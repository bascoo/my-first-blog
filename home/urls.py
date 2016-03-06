from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static, serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$',  views.AgendaView.as_view(), name='event_list'),
    url(r'^(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),   
      
   
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
