from django.urls import path
from django.conf import settings
from . import views
 
 
urlpatterns = [ 
    path(r'', views.home, name="order"),
    path(r'submit', views.submit, name="submit"),
]