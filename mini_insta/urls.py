from django.urls import path
from django.conf import settings
from . import views
 
 
urlpatterns = [ 
    path(r'show_all_profiles', views.home, name="show_all_profiles"),
]