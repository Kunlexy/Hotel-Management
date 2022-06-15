from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Checkin

# Create your views here.
def login(request):
    context= {
        "form" : UserCreationForm()
    }
    return render(request, "account/login.html", context)

def checkin(request):
    if request.method == "POST":
        print("we have made a POST REQUEST")
        room = request.POST.get("room")
        amount = request.POST.get("amount")
        name=request.POST.get("name")
        email=request.POST.get("email")
        occupation=request.POST.get("occupation")
        night=request.POST.get("night")
        start_date=request.POST.get("start_date")
        end_date=request.POST.get("end_date")
        staff=request.user
        checkindetails= Checkin(room = room, amount = amount, name = name, email = email, occupation = occupation, 
        night = night, start_date = start_date, end_date = end_date, staff = staff)
        checkindetails.save()

        
        return redirect("account:checkedview")

    return render(request, "account/checkin.html")

def checkinlist(request):
    checked = Checkin.objects.all()
    context= {
        "checked":checked
    }
    return render(request, "account/checkinlist.html", context)