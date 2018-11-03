from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'listings/listings.html', context)


def listing(request):
    context = {

    }
    return render(request, 'listings/listing.html', context)


def search(request):
    context = {

    }
    return render(request, 'listings/search.html', context)
