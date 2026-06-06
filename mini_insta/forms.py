from django import forms
from .models import *
# File: forms.py
# Author: Taner Altan (altant@bu.edu), 05/29/2026
# Description: forms.py handles forms for new posts like CreatePostForm.


class CreatePostForm(forms.ModelForm):
    '''Handles a form to create a new post in the database'''
    image_url = forms.URLField(label="Image Url", required=False)

    class Meta:
        model = Post
        fields = ['caption']


class UpdatePostForm(forms.ModelForm):
    '''Handles a form to create a new post in the database'''
    image_url = forms.URLField(label="Image Url", required=False)

    class Meta:
        model = Post
        fields = ['caption']

class UpdateProfileForm(forms.ModelForm):
    '''A form to update a quote to the database.'''
 
    class Meta:
        '''associate this form with the Profile model.'''
        model = Profile
        fields = ['display_name','profile_image_url', 'bio_text']

class CreateProfileForm(forms.ModelForm):
    '''A form to handle mutable data about a profile.'''
    class Meta: 
        '''establishes the proper fields.'''
        model = Profile 
        fields = ['username','display_name','profile_image_url', 'bio_text']