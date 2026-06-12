# File: serializers.py
# Author: Taner Altan (altant@bu.edu), 6/12/2026
# Description: responsible for converting Jokes and Pictures to .json


from rest_framework import serializers
from .models import *
 
class JokeSerializer(serializers.ModelSerializer):
  '''
  A serializer for the Joke model.
  Specify which model/fields to send in the API.
  '''
 
  class Meta:
    model = Joke
    fields = ['id', 'text', 'name']
   
  # add methods to customize the Create/Read/Update/Delete operations
  def create(self, validated_data):
    '''
    Override the superclass method that handles object creation.
    '''
    print(f'ArticleSerializer.create, validated_data={validated_data}.')
 
    joke = Joke(**validated_data)
    joke.save()
    return joke
  

class PictureSerializer(serializers.ModelSerializer):
  '''
  A serializer for the Picture model.
  Specify which model/fields to send in the API.
  '''

  class Meta:
    model = Picture
    fields = ['id', 'image_url', 'name', 'timestamp']
   
  # add methods to customize the Create/Read/Update/Delete operations
  def create(self, validated_data):
    '''
    Override the superclass method that handles object creation.
    '''
    print(f'ArticleSerializer.create, validated_data={validated_data}.')
 
    joke = Picture(**validated_data)
    joke.save()
    return joke