from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView


#create your views here


class IndexView(ListView):
    template_name = 'inventory/index.html'
    model = Item
    context_object_name = 'items'




#this incase generic doesn't work for some reason
#def index(request):
#    return render(request, "inventory/index.html")