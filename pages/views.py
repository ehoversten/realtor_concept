from django.shortcuts import render, redirect, HttpResponse


from listings.models import Listing
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings
    }
    return render(request, 'pages/index.html', context)


def about(request):
    context = {

    }
    return render(request, 'pages/about.html', context)
