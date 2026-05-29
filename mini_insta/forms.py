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