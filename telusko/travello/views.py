from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.price = 5000
    dest1.desc = 'the financial capital of India'
    dest1.img = 'destination_1.jpg'
    dest1.offer = False
    

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.price = 650
    dest2.desc = 'First biryani, Then sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.offer = True
    
    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.price = 750
    dest3.desc = 'Beautiful City'
    dest3.img = 'destination_3.jpg'
    dest3.offer = False
    
    dests = [dest1, dest2, dest3]
    
    return render(request, 'index.html', {'dests' : dests})