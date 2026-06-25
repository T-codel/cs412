# File: views.py
# Author: Taner Altan (altant@bu.edu), 6/24/2026
# Description: establishes the views used in the entire project


from typing import Any

from django.shortcuts import render

from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DeleteView, ListView, TemplateView, UpdateView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from project import models
from project.forms import BookRoomForm, CreateProfileViewForm, UpdateProfileViewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date





class ProfileLoginRequiredMixin(LoginRequiredMixin):
    '''Check the request for the logged in user's customer profile.'''
    def logged_prof(self):
        '''Return the customer profile belonging to the logged in user.'''
        return models.Customer.objects.get(user=self.request.user)
    
    def get_login_url(self) -> str:
        '''Return the login URL to send a blocked user to.'''
        return reverse('project_login')

class ShowAllHotelsView(ListView):
    '''Display all hotels in the database.'''
    model = models.Hotel
    template_name = 'project/home.html'
    context_object_name = 'hotels'

class HotelDetailView(DetailView):
    '''DetailView creates a page for every hotel object.'''
    model = models.Hotel
    template_name = 'project/hotel_detail.html'
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        '''Add the rooms' and images' context data to each hotel's page.'''
        context = super().get_context_data(**kwargs)
        context['rooms'] = models.Room.objects.filter(hotel=self.object)
        context['images'] = models.HotelImage.objects.filter(hotel=self.object)
        return context


class BookRoomView(ProfileLoginRequiredMixin, CreateView):
    '''Handle authentification for a customer's attempt to book a room at a hotel.'''
    form_class = BookRoomForm


    template_name = "project/book_room.html"

    def get_login_url(self) -> str:
        '''Return the user to the login page if needed.'''
        return reverse('project_login')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''Add the logged in profile and room being booked by adding them to the context.'''
        context = super().get_context_data(**kwargs)

        context['profile'] = self.logged_prof()

        context['room'] = models.Room.objects.get(pk=self.kwargs['pk'])
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        '''Check for conflicts when attempting to book a hotel as well as invalidates dates in the past. Rejects invalid attempts to book.'''
        room = models.Room.objects.get(pk=self.kwargs['pk'])

        #stores the proposed start and end dates as variables
        start = form.cleaned_data['startDate']
        end = form.cleaned_data['endDate']

        #checks if the start date already happened or if the end date is before the start date. Refuses if either is true 
        if start < date.today() or end <= start:
          return self.handle_no_permission()
        #rejects if already booked.
        if room.is_booked(start,end):
          return self.handle_no_permission()

        #otherwise continue with the form as usual.
        form.instance.customer = self.logged_prof()
        form.instance.room = room
        return super().form_valid(form)

    def get_success_url(self):
        '''Redirect to the list of booked rooms after booking.'''
        return reverse('bookedList')
            



class CancelBookingView(DeleteView):
    '''Handle canceling a booked room.'''
    model = models.BookedRoom
    template_name = 'project/cancel_room.html'
    context_object_name = 'booking'

    def get_success_url(self) -> str:
        '''Redirect to the list of booked rooms.'''
        return reverse('bookedList')


class ShowBookedHotelsView(ProfileLoginRequiredMixin,ListView):
    '''Display the logged in user's rooms'''
    model = models.BookedRoom
    template_name = 'project/booked_rooms.html'
    context_object_name = 'bookings'

    def get_queryset(self) -> QuerySet[Any]:
        '''Return bookings from the logged in customer.'''
        return self.logged_prof().get_all_booked()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''Add a customer's profile information to the context.'''
        context = super().get_context_data(**kwargs)
        context['profile'] = self.logged_prof()
        return context

class LoggedProfileView(ProfileLoginRequiredMixin, DetailView):
    '''Handle each customers' profile page.'''
    model = models.Customer
    template_name = 'project/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        '''Return the logged in customer object.'''
        return self.logged_prof()

class UpdateProfileView(ProfileLoginRequiredMixin, UpdateView):
    '''Update the customer's profile information.'''
    model = models.Customer
    form_class = UpdateProfileViewForm
    template_name = 'project/update_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        '''Return the logged in customer object'''
        # Important for getting the current profile information for updating a profile.
        return self.logged_prof()

    def get_success_url(self) -> str:
        '''Route to the customer's profile page after updating.'''
        return reverse('project_profile')

class CreateProfileView(CreateView):
    '''Use to add a blank user to the context so that the form that creates a new Customer account can store the given information.'''
    model = models.Customer
    form_class = CreateProfileViewForm
    template_name = 'project/create_profile_form.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''Add an empty UserCreationForm form for use in the context to render account and profile fields.'''
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserCreationForm
        return context

    def form_valid(self, form):
        '''Create the user object and then link it to the profile. Logs them in too.'''
        new_form = UserCreationForm(self.request.POST)
        user = new_form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        form.instance.user = user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        '''Specify the url path this corresponds to.'''
        return reverse('project_profile')



class SearchHotelsView(ListView):
    '''Handles searching logic.'''
    model = models.Hotel
    template_name = 'project/search_results.html'
    context_object_name = 'hotels'

    def dispatch(self, request, *args, **kwargs):
        '''Show the search search text box if the user has not searched otherwise run the search.'''
        if 'query' not in self.request.GET:
            return render(request, 'project/search.html', {})
        else: 
            return super().dispatch(request, *args, **kwargs)
        
    def get_queryset(self):
        '''Perform the actual search query.'''
        #gets the proper query value
        query = self.request.GET.get('query','')

        #gets the min price
        min_price = self.request.GET.get('min_price','')

        #gets the max price
        max_price = self.request.GET.get('max_price','')
        
        #does the search without price filters.
        initSearch = models.Hotel.objects.filter(location__icontains=query)

        #limits the search by the min and max price variables.
        if min_price != '':
            initSearch = initSearch.filter(StartingPrice__gte=min_price)
        if max_price != '':
            initSearch = initSearch.filter(StartingPrice__lte=max_price)

        #returns the result. [:50] Limits the results by the first 50.
        return initSearch[:50]
        
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''Add the results of said search query to the html.'''
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query','')
        context['query'] = query
        #uses the previously established filtering information to store the data within the hotels context variable
        context['hotels'] = self.get_queryset()
        context['min_price'] = self.request.GET.get('min_price','')
        context['max_price'] = self.request.GET.get('max_price','')
        return context



