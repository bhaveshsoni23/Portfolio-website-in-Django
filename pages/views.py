from django.shortcuts import render
from django.http import HttpResponse


from listings.models import Listing
from realtors.models import Realtor

def index(request):

    return render(request,'pages/index.html')

def about(request):

    return render(request,'pages/about.html')
