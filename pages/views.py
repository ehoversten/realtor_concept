from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {
    
    }
    return render(request, 'pages/index.html', context)


def about(request):
    context = {

    }
    return render(request, 'pages/about.html', context)
