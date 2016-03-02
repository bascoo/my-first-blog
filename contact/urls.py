from . import views
from django.conf.urls import url


urlpatterns = [ 
		
		 url(r'^$', views.contact, name='contact'),
	]