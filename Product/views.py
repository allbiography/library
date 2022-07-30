from django.shortcuts import render
from .models import *
from .forms import OrderForm
# from .forms import OrderForm, UserChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from . resources import Programming_BookResource


# change password with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'change_pass.html', {'form': fm})
    else:
        return HttpResponseRedirect("")


#
# def user_profile(request):
#     fm = EditUserProfileForm(instance=request.user)
#     return render(request, 'profile.html', {'name': request.user, 'form': fm})


def user_profile(request):
    if request.user.is_authenticated:
        context = {
            'user': request.user
        }
        return render(request, 'profile.html', context)
    else:
        return HttpResponseRedirect("")


def history(request):
    context = {
        'names': book_order
    }
    return render(request, 'history.html', context)


def book_order(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = OrderForm(request.POST, instance=request.user.personal_info)
            if fm.is_valid():
                fm.save()
                return render(request, 'after_book_submitted.html', {})
        else:
            fm = OrderForm(instance=request.user.personal_info)
        return render(request, 'book_order.html', {'name': request.user.personal_info, 'form': fm})
    else:
        return HttpResponseRedirect("")


def search(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            searched = request.POST['searched']
            text_books = Text_Book.objects.filter(name__contains=searched)
            # novels = Novel.objects.filter(name__contains=searched)
            programming_books = Programming_Book.objects.filter(name__contains=searched)
            return render(request, 'search.html', {'searched': searched, 'text_books': text_books,
                                                   'programming_books': programming_books, })
        else:
            return render(request, '', {})
    else:
        return HttpResponseRedirect("")


def description(request):
    if request.user.is_authenticated:
        text_books = Text_Book.objects.all()
        return render(request, 'description.html', {'text_books': text_books})
    else:
        return HttpResponseRedirect("")


def index_programming_book(request):
    if request.user.is_authenticated:
        programming_books = Programming_Book.objects.all()
        return render(request, 'home.html', {'programming_books': programming_books})
    else:
        return HttpResponseRedirect("")


def index_text_book(request):
    if request.user.is_authenticated:
        text_books = Text_Book.objects.all()
        return render(request, 'home.html', {'text_books': text_books})
    else:
        return HttpResponseRedirect("")


# def index_novel(request):
#     novels = Novels.objects.all()
#     return render(request, 'home.html', {'novels': novels})
