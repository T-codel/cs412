import random
from typing import Any

from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DeleteView, ListView, UpdateView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic.detail import SingleObjectMixin
from .forms import CreatePostForm, UpdateProfileForm
from . import models
from .forms import UpdatePostForm

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
    '''subclass for displaying a post'''

    # retrieve objects of type Post from the database
    model = models.Post

    #associate an html file to render with the context from the class.
    template_name = 'mini_insta/show_post.html'
    
    # name for html variable storing the information in the html file.
    context_object_name = 'post'


class CreatePostView(CreateView):
    '''subclass for displaying a create post page'''

    # 
    form_class = CreatePostForm

    #associate an html file to render with the context from the class.
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''Return the context, but with the proper profile context added.'''
        context = super().get_context_data(**kwargs)
        profile = self.kwargs['pk']
        context['profile'] = models.Profile.objects.get(pk=profile)
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        '''attaches a profile to a new form post and uses the inputted image to render.'''
        profile = self.kwargs['pk']
        form.instance.profile = models.Profile.objects.get(pk=profile)
        Uform = form.save()
        image_url = self.request.POST['image_url']
        models.Photo.objects.create(post=Uform, image_url=image_url)
        return super().form_valid(form)

class UpdateProfileView(UpdateView):
    '''A view to update an Profile and save it to the database.'''
 
    model = models.Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"
    
    def form_valid(self, form):
        '''
        Handle the form submission to create a new Article object.
        '''
        print(f'UpdateProfileView: form.cleaned_data={form.cleaned_data}')
 
 
        return super().form_valid(form)
    

class DeletePostView(DeleteView):
    '''subclass for displaying a post'''

    # retrieve objects of type Post from the database
    model = models.Post

    #associate an html file to render with the context from the class.
    template_name = 'mini_insta/delete_post_form.html'
    
    # name for html variable storing the information in the html file.
    context_object_name = 'post'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        #get the default context
        context = super().get_context_data(**kwargs)

        context['profile'] = self.object.profile
        return context
    
    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''
 
 
        # get the pk for this post
        pk = self.kwargs.get('pk')

        post = models.Profile.objects.get(pk=pk)
        # reverse to show the user's profile.
        return reverse('post', kwargs={'pk':post.profile.pk})
    

class UpdatePostView(UpdateView):
    '''subclass for displaying a post'''

    # retrieve objects of type Post from the database
    model = models.Post
    
    form_class = UpdatePostForm
    
    #associate an html file to render with the context from the class.
    template_name = 'mini_insta/update_post_form.html'
    
    # name for html variable storing the information in the html file.
    context_object_name = 'post'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        #get the default context
        context = super().get_context_data(**kwargs)

        context['profile'] = self.object.profile
        return context
    
    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''
 
 
        # get the pk for this post
        pk = self.kwargs.get('pk')

        post = models.Profile.objects.get(pk=pk)
        # reverse to show the user's profile.
        return reverse('post', kwargs={'pk':post.profile.pk})