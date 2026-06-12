# File: views.py
# Author: Taner Altan (altant@bu.edu), 6/12/2026
# Description: basic templates from previous assignments used to create the basic Django views.


import math
import random
from rest_framework import serializers, generics

from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from dadjokes.models import Joke, Picture
from dadjokes.serializers import JokeSerializer, PictureSerializer

class RandomJokeView(TemplateView):
    '''subclass for displaying a random joke'''
    model = Joke

    #associate an html file to render with the context from the class.
    template_name = "dadjokes/random.html"

    context_object_name = "random"
    def get_context_data(self, **kwargs):
        '''returns a random joke'''
        context = super().get_context_data(**kwargs)
        context['joke'] = random.choice(Joke.objects.all())
        context['picture'] = random.choice(Picture.objects.all())
        return context


class ShowJokesView(ListView):
    '''subclass for displaying a random joke'''

    #attribute a model
    model = Joke

    #associate an html file to render with the context from the class.
    template_name = "dadjokes/show_jokes.html"

    #name to be used in html
    context_object_name = "jokes"


class ShowJokeView(DetailView):
    '''subclass for displaying a random joke'''

    model = Joke

    #associate an html file to render with the context from the class.
    template_name = "dadjokes/joke.html"

    #name to be used in html
    context_object_name = "joke"

class ShowPicturesView(ListView):
    '''subclass for displaying a random joke'''

    model = Picture

    #associate an html file to render with the context from the class.
    template_name = "dadjokes/show_pictures.html"

    context_object_name = "pictures"


class ShowPictureView(DetailView):
    '''generates a page for each pk id. Wires the Picture Model to the picture html and picture url'''

    #attribute the proper picture
    model = Picture

    #wire the proper template to show a picture
    template_name = "dadjokes/picture.html"

    #associated url name
    context_object_name = "picture"


class JokesListAPIView(generics.ListCreateAPIView):
  '''
  An API view to return a listing of Jokes
  '''
  queryset = Joke.objects.all()
  serializer_class = JokeSerializer
 
class PicturesListAPIView(generics.ListCreateAPIView):
  '''
  An API view to return a listing of Pictures
  '''
  queryset = Picture.objects.all()
  serializer_class = PictureSerializer
 

class JokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  '''
  An API view to return a random Joke from a list of jokes. Used for specific Joke pages
  '''
  queryset = Joke.objects.all()
  serializer_class = JokeSerializer
    


class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
  '''
  An API view to return a random Joke from a list of jokes. Used for specific Picture pages
  '''
  queryset = Picture.objects.all()
  serializer_class = PictureSerializer


class RandomTemplateAPIView(generics.RetrieveAPIView):
  '''
  An API view to return a random Joke
  '''
  serializer_class = JokeSerializer

  def get_object(self):
    '''overrides get_object to instead get a random object when we're using a random Picture api'''
    return random.choice(Joke.objects.all())
     
class RandomPictureAPIView(generics.RetrieveAPIView):
  '''
  An API view to return a random Picture
  '''
  serializer_class = PictureSerializer

  def get_object(self):
    '''overrides get_object to instead get a random object when we're using a random Picture api'''
    return random.choice(Picture.objects.all())