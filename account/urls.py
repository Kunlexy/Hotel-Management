from django.urls import path
from django.contrib.auth import views as auth_views
from .views import checkin, checkinlist

app_name= "account"

urlpatterns=[
    path('', auth_views.LoginView.as_view(template_name ='account/login.html'), name="loginview"),
    path('logout/', auth_views.LogoutView.as_view(template_name ='account/logout.html'), name="logoutview"),
    path('checkin/', checkin, name="checkinview"),
    path('checkinlist/', checkinlist, name="checkedview")
    
]