from django.urls import path
from . import views
app_name = "inventory"

urlpatterns = [
    path('index/', views.IndexView.as_view(), name="index"),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
   # path('index/', views.index, name="index"),
]