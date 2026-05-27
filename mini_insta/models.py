from django.db import models

# File: urls.py
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

    
    def __str__(self):
        '''Establishes a string representation of the profile object'''

        #prints in the folowing format: username, display name, url, bio, join date
        return f'username: {self.username},display_name: {self.display_name},profile_image_url: {self.profile_image_url},bio_text: {self.bio_text},join_date: {self.join_date},' 
