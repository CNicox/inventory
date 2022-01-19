from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.contrib.auth.backends import BaseBackend


#create your views here


#class MyBackend(BaseBackend):
#    def authenticate(self, request, username=None, password=None):

class IndexView(ListView):
    template_name = 'inventory/index.html'
    model = Item
    context_object_name = 'items'
    paginate_by = 3






#this incase generic doesn't work for some reason
#def index(request):
#    return render(request, "inventory/index.html")