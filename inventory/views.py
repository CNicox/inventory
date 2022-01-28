from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, TemplateView
from django.contrib.auth.backends import BaseBackend
from .forms import *
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth import login, authenticate  # add this


# create your views here


# class MyBackend(BaseBackend):
#    def authenticate(self, request, username=None, password=None):

class IndexView(ListView):
    template_name = 'inventory/index.html'
    model = Item
    context_object_name = 'items'
    paginate_by = 3


# ne rabotaet ne ebu pochemu
# update: rabotaet (ebu pochemu)
class RegistrationView(TemplateView):
    template_name = 'registration/create_user.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.clean_password2()
            form.save()
            return redirect('/inventory/registration/')

        args = {'form': form}
        return render(request, self.template_name, args)


class ChangePasswordView(TemplateView):
    template_name = '/inventory/change_password.html'

    def get(self, request):
        form = UserChangeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.clean_password()
            form.save()
            return redirect('/inventory/change-password/')

        args = {'form': form}
        return render(request, self.template_name, args)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {email}.")
                return redirect("/inventory/registration/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"form": form})


# def registration_form_post(request):
#    form = UserCreationForm()
#    # if form.is_valid():
#    #   form.save()
#    return render(request, 'registration/create_user.html', {'form': form})


'''

    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            print(email, password1, password2)
'''

# this incase generic doesn't work for some reason
# def index(request):
#    return render(request, "inventory/index.html")
