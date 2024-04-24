from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, "HomePage/index.html")

def index5(request):
    return render(request, "HomePage/index.html")