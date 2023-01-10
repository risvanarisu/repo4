from django.shortcuts import render

# Create your views here.
def registermanager(request):
    return render(request,"manager/attendance.html")
