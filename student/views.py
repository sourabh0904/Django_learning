from django.shortcuts import render

# Create your views here.
def Hello_students(request) :
    return render(request ,"student.html")

def StudentDashboard(request) :
    return render(request , "dashboard.html")