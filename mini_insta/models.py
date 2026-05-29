from django.db import models
from django.urls import reverse

# File: models.py
# Author: Taner Altan (altant@bu.edu), 05/26/2026
# Description: models.py estabilishes the datastructure of the data stored in sqlite3 for the website.



# Create your models here.
class Profile(models.Model):
    '''Create a model called Porfile storing information about a person.'''

    #establishes a column storing a username
    username = models.TextField(blank=False)

    #establishes a column storing a display name
    display_name = models.TextField(blank=False)

    #establishes a column storing a url to a profile picture
    profile_image_url = models.URLField(blank=False)

    #establishes bio_text for their profile. (I made mine quite limited to be fair.)
    bio_text = models.TextField(blank=False)

    #Lists the join date of the user.
    join_date = models.DateField(auto_now=True)

    def get_all_posts(self):
        '''returns a list of all posts form the profile object'''
        return Post.objects.filter(profile=self).order_by("timestamp")

    
    def __str__(self):
        '''Establishes a string representation of the profile object'''

        #prints in the folowing format: username, display name, url, bio, join date
        return f'username: {self.username},display_name: {self.display_name},profile_image_url: {self.profile_image_url},bio_text: {self.bio_text},join_date: {self.join_date},' 



class Post(models.Model):
    '''class used to represent a user's post'''
    profile = models.ForeignKey("Profile",on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this Comment object.'''
        return f'{self.caption}'
    
    def get_all_photos(self):
        '''returns a list of all photos form the post object'''
        return Photo.objects.filter(post=self).order_by("timestamp")

    def get_absolute_url(self):
        '''returns the url of the post object'''
        return reverse('post', kwargs={'pk':self.pk})


class Photo(models.Model):
    '''class used to represent a photo contained in a post which can have an arbitrary number of photos'''
    post = models.ForeignKey("Post",on_delete=models.CASCADE)
    image_url = models.TextField(blank=True)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this photo object.'''
        return f'{self.image_url}'