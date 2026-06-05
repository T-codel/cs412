from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

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

    user = models.ForeignKey(User, on_delete=models.CASCADE) ## NEW


    def get_all_posts(self):
        '''returns a list of all posts form the profile object'''
        return Post.objects.filter(profile=self).order_by("timestamp")

    
    def __str__(self):
        '''Establishes a string representation of the profile object'''

        #prints in the folowing format: username, display name, url, bio, join date
        return f'username: {self.username},display_name: {self.display_name},profile_image_url: {self.profile_image_url},bio_text: {self.bio_text},join_date: {self.join_date},'

    def get_absolute_url(self):
        return "/mini_insta/profile/%i/" % self.pk 

    def get_followers(self):
        '''returns a list of all photos form the post object'''
        followers = Follow.objects.filter(profile=self)

        l = []
        for follower in followers:
            l.append(follower.follower_profile)

        return l
    
    def get_num_followers(self):
        followers = Follow.objects.filter(profile=self)
        return followers.count()

    def get_following(self):
        people = Follow.objects.filter(follower_profile=self)

        l = []
        for person in people:
            l.append(person.profile)

        return l

    def get_num_following(self):
        followers = Follow.objects.filter(follower_profile=self)
        return followers.count()
    
    def get_post_feed(self):
        following = self.get_following()
        return Post.objects.filter(profile__in=following).order_by("timestamp")


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

    def get_all_comments(self):
        '''returns all comments on a post'''
        comments = Comment.objects.filter(post=self)
        return comments.order_by("timestamp")

    def get_all_likes(self):
        '''returns all likes on a post. Notably includes who did it'''
        likes = Like.objects.filter(post=self)
        return likes.order_by("timestamp")


class Photo(models.Model):
    '''class used to represent a photo contained in a post which can have an arbitrary number of photos'''
    post = models.ForeignKey("Post",on_delete=models.CASCADE)
    image_url = models.TextField(blank=True)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this photo object.'''
        return f'{self.image_url}'
    
class Follow(models.Model):
    '''class used to represent a photo contained in a post which can have an arbitrary number of photos'''
    profile = models.ForeignKey("Profile",related_name="follower",on_delete=models.CASCADE)
    follower_profile = models.ForeignKey("Profile",related_name="follower_profile",on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this photo object.'''
        return f'{self.follower_profile} follows {self.profile}'


class Comment(models.Model):
    post = models.ForeignKey("Post",related_name="post_comments",on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile",related_name="comments",on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now=True)
    text = models.TextField(blank=False)

    def __str__(self):
        '''Return a string representation of this photo object.'''
        return f'{self.profile} says {self.text} at {self.timestamp}'
    

class Like(models.Model):
    post = models.ForeignKey("Post",related_name="post_likes",on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile",related_name="like",on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this photo object.'''
        return f'{self.profile} likes {self.post}'

class ProfileLoginRequiredMixin(LoginRequiredMixin):
    '''uses the hint to create a class that erturns the current user.'''
    def logged_prof(self):
        return Profile.objects.get(user=self.request.user)
    
    def get_login_url(self) -> str:
        return reverse('login')
