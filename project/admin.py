# File: apps.py
# Author: Taner Altan (altant@bu.edu), 6/25/2026
# Description: establishes the models to be used by django admin.


from django.contrib import admin

from project.models import BookedRoom, Customer, Hotel, HotelImage, Room

# Register your models here.


admin.site.register(Customer)
admin.site.register(Hotel)
admin.site.register(HotelImage)
admin.site.register(Room)
admin.site.register(BookedRoom)