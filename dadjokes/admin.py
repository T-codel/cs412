# File: admin.py
# Author: Taner Altan (altant@bu.edu), 6/12/2026
# Description: register the models so they can be modified by the django admin.


from django.contrib import admin

from dadjokes.models import Joke, Picture

# Register your models here.
admin.site.register(Joke)
admin.site.register(Picture)
