from django.contrib import admin

from dadjokes.models import Joke, Picture

# Register your models here.
admin.site.register(Joke)
admin.site.register(Picture)
