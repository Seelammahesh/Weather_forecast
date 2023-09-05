"""weather_forecast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from datainfo.views import add_state,add_district,update_district,list_district,delete_district,update_state,list_state,delete_state

urlpatterns = [
    path('admin/', admin.site.urls),
    #state
    path('add_state/',add_state,name="add_state"),
    path('update_state/',update_state,name="update_state"),
    path('list_state/',list_state,name="list_state"),
    path('delete_state/',delete_state,name="delete_state"),
    #district
    path('add_district/',add_district,name="add_district"),
    path('update_district/',update_district,name="update_district"),
    path('list_district/',list_district,name="list_district"),
    path('delete_district/',delete_district,name="delete_district"),

]
