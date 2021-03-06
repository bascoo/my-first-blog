from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from .home import views 

urlpatterns = [
    url(r'^$', include('home.urls', namespace="home")),
    url(r'^stories/', 'home.views.verhalen'),
    url(r'^overons/', 'home.views.aboutus'), 
    url(r'^colofon/', 'home.views.colofon'), 
	url(r'^durfjij/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^contact/', include('contact.urls', namespace="contact")),  
    url(r'^iamgrey/', include('iamgrey.urls', namespace="iamgrey")), 
    url(r'^partners/', include('partners.urls', namespace="partners")), 
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
