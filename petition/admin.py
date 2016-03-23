from django.contrib import admin
from .models import Petition, Vote
# Register your models here.



class VoteInline(admin.TabularInline):
	model = Vote
	extra = 1

class PetitionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['petition_title']}),
        ('Petition text' ,{'fields': ['petition_text'], 'classes': ['collapse']}),
    ]
    inlines = [VoteInline]
    list_display = ('petition_title', 'petition_text' )
    search_fields = ['petition_text']

admin.site.register(Petition, PetitionAdmin)

