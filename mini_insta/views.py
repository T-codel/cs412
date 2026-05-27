import random

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from . import models


# Create your views here.
class ShowAllView(ListView):
    '''Create a subclass of ListView to display all blog articles.'''
 
 
    model = models.Profile # retrieve objects of type Article from the database
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles' # how to find the data in the template file



def home(request):
    '''Define a view to show the 'home.html' template.'''
 
 
    # the template to which we will delegate the work
    template = 'mini_insta/show_all_profiles.html'
 
 
    images = {
        'image1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Mikhail_Tal_1962.jpg/330px-Mikhail_Tal_1962.jpg',
        'image2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Wereldkandidaten_schaaktoernooi_in_Zuid_Slavia_Tal_%28Rusland%29%2C_Petrosjan_%28Rusland%2C_Bestanddeelnr_910-7198.jpg/330px-Wereldkandidaten_schaaktoernooi_in_Zuid_Slavia_Tal_%28Rusland%29%2C_Petrosjan_%28Rusland%2C_Bestanddeelnr_910-7198.jpg',
        'image3' : 'https://i.pinimg.com/236x/10/e2/1f/10e21f1857861117d96a503fd255bcf5.jpg',
    }
    quotes = {
        'quote1' : "“You must take your opponent into a deep dark forest where 2+2=5, and the path leading out is only wide enough for one.”",
        'quote2' : "“To play for a draw, at any rate with white, is to some degree a crime against chess.”",
        'quote3' : "“There are two types of sacrifices: correct ones, and mine.”",
    }


    # a dict of key/value pairs, to be available for use in template
    context = {
        'image' : random.choice(list(images.values())),
        'quote' : random.choice(list(quotes.values())),

    }
 
 
    return render(request, template, context)
