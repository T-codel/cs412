# File: models.py
# Author: Taner Altan (altant@bu.edu), 6/18/2026
# Description: establishes the models used throughout the entire project


import random

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Customer(models.Model):
    '''Create the Customer model connected to a django user.'''

    #stores the first name
    firstName = models.TextField(blank=False)

    #stores the last name
    lastName = models.TextField(blank=False)

    #stores a user's address. Will need to be validated.
    Address = models.TextField(blank=False)

    #stores the email
    email = models.TextField(blank=False)

    #stores the user's information to sell to advertisers (joking obviously)
    dateOfBirth = models.DateField()

    #stores the phone number
    phoneNumber = models.TextField(blank=False)

    #associates a customer with an account object
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        '''Return the logged in user's profile url.'''
        return reverse('project_profile')
    
    def get_all_booked(self):
        '''Return the logged in user's booked rooms ordered by start date.'''
        return BookedRoom.objects.filter(customer=self).order_by("startDate")


class Hotel(models.Model):
    '''Create the Hotel model.'''

    #stores the hotel name
    name = models.TextField(blank=False)

    #stores the hotel location
    location = models.TextField(blank=False)

    #stores the cumulative rating.
    Rating = models.DecimalField(blank=False, max_digits=2, decimal_places=1)

    #stores the starting price
    StartingPrice = models.DecimalField(blank=False,max_digits=8,decimal_places=2)

    #stores the phone number
    phoneNumber = models.TextField(blank=False)

    def get_absolute_url(self):
        '''Return Hotel object's detail page.'''
        return reverse('currentHotel', kwargs={'pk': self.pk})
    
    def get_all_images(self):
        '''Return the Hotel object's images.'''
        return HotelImage.objects.filter(hotel=self).order_by("-datePosted")
    
    def get_all_rooms(self):
        '''Return all of the Hotel object's rooms.'''
        return Room.objects.filter(hotel=self).order_by("roomNum")



class HotelImage(models.Model):
    '''Create the HotelImage Model to represent a hotel having multiple images.'''

    #stores the hotel the image is associated with
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    #stores when the image was posted
    datePosted = models.DateField(auto_now=True)

    #stores the image file itself
    imageFile = models.TextField(blank=False)




class Room(models.Model):
    '''Create the Room Model to represent a hotel having multiple rooms.'''


    #associaes the room with the hotel
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    #Used to store the room type
    type = models.TextField(blank=False)

    #the floor
    floor = models.TextField(max_length=10)

    #stores the room's number.
    roomNum = models.IntegerField()

    #stores the price
    RoomPrice = models.DecimalField(blank=False,max_digits=8,decimal_places=2)


    def get_absolute_url(self):
        '''Return the page used to book the room object.'''
        return reverse('currentBook', kwargs={'pk' : self.pk})

    def is_booked(self,startDate, endDate):
        '''Return true if overlap exists with other booked times.'''
        boole = BookedRoom.objects.filter(room=self).filter(startDate__lt=endDate).filter(endDate__gt=startDate)
        return boole.exists()


class BookedRoom(models.Model):
    '''Create the BookedRoom Model to represent a hotel having multiple booked room.'''



    #keeps track of the customer who is booked into a room
    customer = models.ForeignKey(Customer,  on_delete=models.CASCADE)

    #keeps track of the room a customer is booked into
    room = models.ForeignKey(Room,  on_delete=models.CASCADE)

    #responsible for storing the start date
    startDate = models.DateField()

    #responsible for storing the end date
    endDate = models.DateField()

    def getRoom(self):
        '''Return the room object that is booked.'''
        return self.room
    
    def getCustomer(self):
        '''Return the customer object that booked the room.'''
        return self.customer
    
    def getNights(self):
        '''Return the number of nights.'''
        return (self.endDate - self.startDate).days
    
    def getPrice(self):
        '''Return the total price of the booked room.'''
        return self.getNights() * self.room.RoomPrice


def load_data():
    '''Function to load data records from CSV file into Django model instances.'''
 
    filename = '/Users/taneraltan/Downloads/hotels(4).csv'
    f = open(filename)
    f.readline() # discard headers
 
    for row in f:
 
        line = row.strip()
        fields = line.split(',')
        try:
            result = Hotel(
                name=fields[0],
                location=fields[1],
                Rating=fields[2],
                StartingPrice = fields[3],
                phoneNumber = fields[4],
            )

            result2 = HotelImage(
                hotel=result,
                imageFile = fields[5],
            )
            result.save() # commit to database
            result2.save()

            if len(Hotel.objects.all()) > 35000:
                result3 = HotelImage(
                    hotel=result,
                    imageFile = oldImage,
                )
                result3.save()
            oldImage = fields[5]


            print(f'Created result: {result}')
                
        except:
            print(f"Skipped: {fields}")
    
    print(f'Done. Created {len(Hotel.objects.all())} Hotels.')


def addNumbers():
    '''Function to add random numbers to the hotels in the database.'''
    for hotel in Hotel.objects.all():
        hotel.phoneNumber = str(random.randint(1000000000,9999999999))
        hotel.save()

def loadRooms():
    '''Function to load data records from CSV file into Django model instances.'''
 
    filename = '/Users/taneraltan/Downloads/rooms.csv'
    f = open(filename)
    f.readline() # discard headers
 
    #loops through each room in the csv.
    for row in f:
        line = row.strip()
        fields = line.split(',')
        try:
            #generates models from said rooms
            result = Room(
                hotel=Hotel.objects.get(pk=fields[0]),
                type=fields[1],
                floor=fields[2],
                roomNum=fields[3],
                RoomPrice = fields[4],
            )
            
            result.save() # commit to database

            print(f'Created result: {result}')
                
        except:
            print(f"Skipped: {fields}")
