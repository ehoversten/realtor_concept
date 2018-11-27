from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.

def register(request):
    if request.method == 'POST':
        # ERROR MESSAGES
        # messages.error(request, "Testing error message")

        # GET FORM VALUES 
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['username']
        email      = request.POST['email']
        password   = request.POST['password']
        password2  = request.POST['password2']

        # VALIDATION 
        if password == password2:
            # CHECK USERNAME UNIQUNESS
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken, please choose another")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already registered")
                    return redirect('register')
                else:
                    # EVERYTHING OK
                    user = User.objects.create_user(first_name= first_name, last_name=last_name, username=username, email=email, password=password)
                    # LOGIN AFTER SUCCESSFUL REGISTRATION
                    # auth.login(request, user)
                    # messages.success(request, "You are now logged in")
                    # return redirect('index') 

                    # SAVE USER DO NOT LOGIN
                    user.save()
                    messages.success(request, "You are now registered, please log in")
                    return redirect('login')

            
        else:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # REGISTER USER
        # print('POST SUBMITTED REG')
        # return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # GET FORM VALUES
        username = request.POST['username']
        password = request.POST['password']

        # AUTHENTICATE USER
        user = auth.authenticate(username=username, password=password)
        # USER EXISTS - LOGIN USER
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are now logged out")
    
        return redirect('index')


def dashboard(request):
    # find logged in user and query for any submitted contacts
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
