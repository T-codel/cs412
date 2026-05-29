import random
from typing import Any

from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic.detail import SingleObjectMixin
from .forms import CreatePostForm
from . import models

# File: views.py
# Author: Taner Altan (altant@bu.edu), 05/27/2026
# Description: views.py is responsible for generating context needed to properly render webpages


# Create a class extending listView
class ShowAllView(ListView):
    '''Create a subclass of ListView to display all Profiles.'''
    # retrieve objects of type Profile from the database
    model = models.Profile 

    #associate an html file to render with the context from the profile.
    template_name = 'mini_insta/show_all_profiles.html'  

    # name for html variable storing the information in the html file.
    context_object_name = 'profiles' 

class ProfileDetailView(DetailView):
    '''Create a subclass of DetailView to display each profile on their own html page.'''
    # retrieve objects of type Profile from the database
    model = models.Profile 

    #associate an html file to render with the context from the profile.
    template_name = 'mini_insta/show_profile.html'
    
    # name for html variable storing the information in the html file.
    context_object_name = 'profile'

class PostDetailView(DetailView):
    model = models.Post

    template_name = 'mini_insta/show_post.html'
    
    context_object_name = 'post'


class CreatePostView(CreateView):
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        profile = self.kwargs['pk']
        context['profile'] = models.Profile.objects.get(pk=profile)
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        profile = self.kwargs['pk']
        form.instance.profile = models.Profile.objects.get(pk=profile)
        Uform = form.save()
        image_url = self.request.POST['image_url']
        models.Photo.objects.create(post=Uform, image_url=image_url)
        return super().form_valid(form)
