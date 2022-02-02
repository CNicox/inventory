from django.urls import path
from . import views
app_name = "inventory"

urlpatterns = [
    path('index/', views.IndexView.as_view(), name="index"),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    #path("login/", views.login_request, name="login"),
    path('index/', views.index, name="index"),
]