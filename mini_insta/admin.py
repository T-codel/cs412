from django.contrib import admin

from .models import Follow, Profile, Comment, Like
from .models import Post
from .models import Photo


# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Like)