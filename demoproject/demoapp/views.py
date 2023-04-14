from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
# Create your views here.

def home(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})


# def about(request):
#     return render(request,"inddd.html")
# def contact(request):
#     return render(request,"cont.html")
# def details(request):
#     return render(request,"det.html")
# def thanks(request):
