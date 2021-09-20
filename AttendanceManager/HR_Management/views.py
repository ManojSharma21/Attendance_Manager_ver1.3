from django.shortcuts import render
from .models import Daily_Attendance,Employees_Detail
from datetime import datetime
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import RegisterForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    if request.method == "POST":
        Username=request.POST.get("username")
        Password = request.POST.get("Password")
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            time_out=Daily_Attendance.objects.filter(Employee_Id_id=int(Username),Time_out=None).first()

            if time_out is not None :
                time_out.Time_out=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                time_out.save()
                return render(request, "success_exit.html")

            else:
                send_data = Daily_Attendance(Employee_Id_id=Username, Time_in=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), Status="Present")
                send_data.save()
                return render(request, "success_entry.html")

        else:
            return render(request, "invalidid.html")

    return render(request, "index.html")

def Register(request):
    submitted = False
    if request.method== "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/register?submitted=True")
    else:
        form= RegisterForm
        if "submitted" in request.GET:
            submitted=True

    return render(request,"register.html",{"form":form,"submitted":submitted})
