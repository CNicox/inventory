from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.contrib.auth.backends import BaseBackend
from .forms import *


#create your views here


#class MyBackend(BaseBackend):
#    def authenticate(self, request, username=None, password=None):

class IndexView(ListView):
    template_name = 'inventory/index.html'
    model = Item
    context_object_name = 'items'
    paginate_by = 3


def registration_form(request):

    form = UserCreationForm()
    return render(request, 'create_user.html', {'form' : form})
'''

    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            print(email, password1, password2)
'''





#this incase generic doesn't work for some reason
#def index(request):
#    return render(request, "inventory/index.html")