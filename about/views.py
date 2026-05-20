import random
import time

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
 
 
# Create your views here.
 
 
def home(request):
    '''Define a view to show the 'home.html' template.'''
 
 
    # the template to which we will delegate the work
    template = 'about/about.html'
 
 
    # a dict of key/value pairs, to be available for use in template
    context = {}
 
 
    return render(request, template, context)
