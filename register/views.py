from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration Successful!')
            return redirect('/login/')
        
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')

    else:
        form = RegisterForm()
    
    context = {
        'form':form
    }
    return render(request, 'register/register.html', context)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()

    context = {
        'login_form':form
    }

    return render(request, 'registration/login.html', context)



def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('/login/')