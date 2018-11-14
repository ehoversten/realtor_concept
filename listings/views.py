from django.shortcuts import render, redirect

from .models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.all()
    context = {
        'listings':listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    context = {

    }
    return render(request, 'listings/listing.html', context)


def search(request):
    context = {

    }
    return render(request, 'listings/search.html', context)
