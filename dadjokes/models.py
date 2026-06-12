# File: models.py
# Author: Taner Altan (altant@bu.edu), 6/12/2026
# Description: establishes the two models used throughout the entire project


from django.db import models

# Create your models here.


class Joke(models.Model):
    text = models.TextField(blank=False)
    name = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.text


class Picture(models.Model):
    image_url = models.URLField(blank=False)
    name = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)
