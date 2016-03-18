from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from .models import Partner

class IndexView(generic.ListView):
    template_name = 'partner/partner_list.html'
    context_object_name = 'latest_partner_list'

    def get_queryset(self):
        return Partner.objects.filter(date_published__lte=timezone.now()).order_by('name')
