from django.urls import path
from django.conf import settings
from . import views
from .views import SearchView, ShowAllView, ShowFeedView, UpdateProfileView
from .views import ProfileDetailView
from .views import PostDetailView
from .views import CreatePostView
from .views import DeletePostView
from .views import UpdatePostView
from .views import ShowFollowersDetailView
from .views import ShowFollowingDetailView

# File: urls.py
# Author: Taner Altan (altant@bu.edu), 05/27/2026
# Description: urls.py is responsible for mapping given urls to the appropriate context. 


urlpatterns = [ 

    # /mini_insta alone directs to an equivalent page to the show_all_profiles page. 
    path('', ShowAllView.as_view(), name='show_all'), # generic class-based view

    # /mini_insta/show_all_profiles sends you to a page containing all profiles. 
    path(r'show_all_profiles', ShowAllView.as_view(), name="show_all_profiles"),
    
    # /mini_insta/profile/x sends you to a page containing a given profile based upon a number. 
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('profile/<int:pk>/create_post', CreatePostView.as_view(), name='create_post'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name='update_post'),
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name="followers"),
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name="following"),
    path('profile/<int:pk>/feed', ShowFeedView.as_view(), name="feed"),
    path('profile/<int:pk>/search', SearchView.as_view(), name="search"),
]