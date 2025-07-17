from django.contrib import admin
from django.contrib import admin
from .models import  *

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Url']
    list_editable = ['Name','Url']
    list_display_links = None
