# File: urls.py
# Author: Taner Altan (altant@bu.edu), 05/27/2026
# Description: urls.py is responsible for mapping given urls to the appropriate context. 


from django.urls import path
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('', views.SearchHotelsView.as_view(), name="project_home"),
    path('home', views.ShowAllHotelsView.as_view(), name="show_all_home"),
    path('hotel/<int:pk>', views.HotelDetailView.as_view(), name="currentHotel"),
    path('book/<int:pk>', views.BookRoomView.as_view(), name="currentBook"),
    path('book/cancel/<int:pk>', views.CancelBookingView.as_view(), name="cancel"),

    path('profile', views.LoggedProfileView.as_view(), name="project_profile"),
    path('updateProfile', views.UpdateProfileView.as_view(), name="project_update_profile"),

    path('bookedList', views.ShowBookedHotelsView.as_view(), name="bookedList"),
    path('createProfile', views.CreateProfileView.as_view(), name="project_create_profile"),

    path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='project_login'), 
	path('logout/', auth_views.LogoutView.as_view(next_page='project_home'), name='project_logout'), 

]