from django.urls import path
from .views import home, contact, about

app_name = "home"

urlpatterns= [

    path('', home, name="homeview"),
    path('contact/', contact, name="contactview"),
    path('about/', about, name="aboutview"),


]