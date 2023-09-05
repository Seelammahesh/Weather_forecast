from django.contrib import admin
from .models import  State,District

# Register your models here.

class StateAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_filter = ['name']
    search_fields = ['name']



class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id','state','name','rainfall_type','created_at','updated_at']
    list_filter = ['name','rainfall_type']
    search_fields = ['name']


admin.site.register(State,StateAdmin),
admin.site.register(District,DistrictAdmin)