from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.TextField(blank=False)
    display_name = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=False)
    bio_text = models.TextField(blank=False)
    join_date = models.DateField(auto_now=True)
    def __str__(self):                
        return f'username: {self.username},display_name: {self.display_name},profile_image_url: {self.profile_image_url},bio_text: {self.bio_text},join_date: {self.join_date},' 
