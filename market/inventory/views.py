from django.http import HttpResponse
from django.shortcuts import render
from inventory.models import Seller, Inventory

#view number 1
def welcome(request):
    inventory = Inventory.objects.all()


    return render(request, 
                 'inventory/welcome.html', 
                 {'inventory': inventory });


#view number 2
def contact(request):
    return render(request, 'inventory/contact.html')


#view number 3
def bye(request):
    return HttpResponse('<h1>Bye</h1>')