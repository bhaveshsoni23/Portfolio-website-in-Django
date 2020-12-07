from django.shortcuts import render


from .models  import Listing


def index(request):
    return render(request , 'listings/listings.html')




