from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.http import HttpResponseRedirect


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('programming_book')
        else:
            # messages.success(request, ("oops! something went wrong, Try again"))
            return redirect('login-user')
        pass
    else:
        return render(request, 'authenticate/main_login_box.html', {})


def logout_user(request):
    logout(request)
    # messages.success(request, ("You Were Logged Out!?"))
    return redirect('login-user')








