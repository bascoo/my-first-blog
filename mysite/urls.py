from django.conf.urls import include, url
from django.contrib import admin
#from .home import views 

urlpatterns = [
    url(r'^$', 'home.views.index'),
	url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
]
