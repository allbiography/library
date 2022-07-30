from django import forms
from django.forms import ModelForm
from .models import personal_info
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class OrderForm(ModelForm):
    class Meta:
        model = personal_info
        fields = ('first_ordered_book', 'second_ordered_book')

        labels = {

            'first_ordered_book': '',
            'second_ordered_book': '',

        }
        widgets = {
            'first_ordered_book': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': '        Enter the name of first book'}),
            'second_ordered_book': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': '        Enter the name of second book'}),

        }
