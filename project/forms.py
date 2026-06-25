# File: forms.py
# Author: Taner Altan (altant@bu.edu), 05/29/2026
# Description: forms.py handles forms for new posts like CreatePostForm.


from django import forms
from .models import *


class BookRoomForm(forms.ModelForm):
    '''Handles a form to create a new post in the database'''
    startDate = forms.DateField(label="Start Date", widget=forms.DateInput(attrs={'type': 'date'}))
    endDate = forms.DateField(label="End Date", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = BookedRoom
        fields = ['startDate', 'endDate']


class UpdateProfileViewForm(forms.ModelForm):
    '''A form to update a quote to the database.'''
 
    class Meta:
        '''associate this form with the Profile model.'''
        model = Customer
        fields = ['firstName','lastName', 'Address', 'email', 'phoneNumber']

class CreateProfileViewForm(forms.ModelForm):
    '''A form to handle mutable data about a profile.'''
    class Meta: 
        '''establishes the proper fields.'''
        model = Customer 
        fields = ['firstName','lastName','Address', 'dateOfBirth', 'phoneNumber', 'email']
        widgets = {
            'firstName': forms.TextInput(),
            'lastName': forms.TextInput(),
            'Address': forms.TextInput(),
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'}),
            'phoneNumber': forms.TextInput(),
            'email' : forms.TextInput()
        }










