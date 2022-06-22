from genericpath import exists
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
    checked = Checkin.objects.all().order_by("-time_checkedin")
    context= {
        "checked":checked
    }
    return render(request, "account/checkinlist.html", context)

def search(request):
    if request.method == "POST":
        occupant_name = request.POST.get("name")
        if Checkin.objects.filter(name = occupant_name).exists():
           name = Checkin.objects.get(name = occupant_name)
        else:
            name = None
        #try:
        #    name = Checkin.objects.get(name = occupant_name)
        #except:
        #    name = None

        context = {
            "name": name
        }
        return render (request, "account/notfound.html", context)
       

    return render(request, "account/search.html")

def notfound(request):
    return render (request, "account/notfound.html")

def update(request):
    if request.method == "POST":
        occupant_name = request.POST.get("name")

        try:
            name = Checkin.objects.get(name = occupant_name)

        except:
            name = None

        context = {
            "name" : name
        }

        return render(request, "account/updetails.html", context)

    return render (request, "account/update.html")

def updetails(request):
    if request.method == "POST":
        room = request.POST.get("room")
        amount = request.POST.get("amount")
        name=request.POST.get("name")
        email=request.POST.get("email")
        occupation=request.POST.get("occupation")
        night=request.POST.get("night")
        start_date=request.POST.get("start_date")
        end_date=request.POST.get("end_date")
        staff=request.user
        id= request.POST.get("ID")

        Checkin.objects.filter(id=id).update(room=room, amount = amount, name=name, email=email, occupation = occupation, 
        night=night,start_date=start_date, end_date=end_date, staff=staff)

        return redirect("account:checkedview")

    return render(request, "account/updetails.html")

def delete_view(request):
    if request.method == "POST":
        occupant_name = request.POST.get("name")

        try:
            name= Checkin.objects.get(name=occupant_name)
        except:
            name = None

        context={

            "name" : name
        }
        
        return render(request, "account/deleting.html", context)

    return render(request, "account/delete.html") 

def deleting(request):
    if request.method == "POST":
        customer_id = request.POST.get("id")
        Checkin.objects.get(id=customer_id).delete()

        return redirect("account:checkedview")
        
    return render(request, "account/deleting.html") 
