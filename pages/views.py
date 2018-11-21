from django.shortcuts import render, redirect, HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    # Get 3 Latest Listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings'       : listings, 
        'state_choices'  : state_choices,
        'price_choices'  : price_choices,
        'bedroom_choices': bedroom_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get Realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP Realtor
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'pages/about.html', context)
