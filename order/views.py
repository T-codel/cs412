import random
import time

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
 
 
# Create your views here.
 
 
def home(request):
    '''Define a view to show the 'home.html' template.'''
 
 
    # the template to which we will delegate the work
    template = 'order/show_form.html'
 

    images = {
        'https://d3ciwvs59ifrt8.cloudfront.net/7ba8800b-91c2-4eb1-9451-4dce61fbd96f/0bb99c35-19c5-4791-a5d9-ec2b256cdda8.jpg': "Grilled Chicken",
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIYXZZNkr_i5t2Y8Y20LehlcZdU-3wd1xwvA&s': "Fried Chicken",
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRD6eZ3VWU21avGxvufQ1uEPG8kSBO1TWwuNA&s': "French Fries",
    }

    special_image = random.choice(list(images.keys()))
    V1 = ""
    V2 = ""
    V1n = ""
    V2n = ""
    for i in images:
        if i != special_image:
            if V1 == "":
                V1 = i
                V1n = images[i]
            else:
                V2 = i
                V2n = images[i]

    

    context = {
        'special' : special_image,
        'specialT' : images[special_image],
        'O1' : V1,
        'O1n' : V1n,
        'O2' : V2,
        'O2n' : V2n

    }
 
 
    return render(request, template, context)


def submit(request):

    template_name = "confirmation/confirmation.html"
    print(request.POST)
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        special = request.POST.get('special','')
        O1 = request.POST.get('O1','')
        O2 = request.POST.get('O2','')
        burger = request.POST.get('burger','')
        beef = request.POST.get('patty1','')
        chicken = request.POST.get('patty2','')
        veggie = request.POST.get('patty3','')
        instructions = request.POST['instructions']
    v = time.time()+random.randint(30,60)*60
    v = time.strftime('%I:%M %p', time.localtime(v))
    context = {
        'name': name,
        'phone': phone,
        'email': email,
        'special': special,
        'O1': O1,
        'O2': O2,
        'burger': burger,
        'beef': beef,
        'chicken': chicken,
        'veggie': veggie,
        'instructions' : instructions,
        'time' : v
    }
    return render(request, template_name, context)
