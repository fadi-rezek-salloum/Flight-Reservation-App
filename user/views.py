from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from user.models import User

def loginView(request):

    if request.method == 'POST':
        user = authenticate(email=request.POST.get('email'), password=request.POST.get('password'))

        if user is not None:
            login(request, user)

            return redirect('/')
        else:
            return HttpResponseNotAllowed('Error!')

    return render(request, 'user/login.html', context={})


def registerView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(username=username, email=email)

        user.set_password(raw_password=password)

        user.save()

        return redirect('/account/login/')

    return render(request, 'user/register.html', context={})

def logoutView(request):
    
    logout(request)

    return redirect('/')