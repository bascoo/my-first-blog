from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'$', views.PetitionView.as_view(), name='petition'),
	url(r'^(?P<petition_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
