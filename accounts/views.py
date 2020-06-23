from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['phoneNumber']
        password1 = request.POST['password']

        user = auth.authenticate(username=username, password=password1)
        print('User logged in!')
        return redirect('dashboard')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['phoneNumber']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name)
        user.save()
        print('User created!')
        return redirect('dashboard')

    else:
        return render(request, 'register.html')


