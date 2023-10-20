from django import forms
from .models import Client, Product


class ClientForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=50)
    image = forms.ImageField(label='Изображение', required=False)
    address = forms.CharField(label='Адрес', max_length=100)


class ProductForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100)
    description = forms.CharField(label='Описание', widget=forms.Textarea)
    price = forms.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    count_product = forms.IntegerField(label='Количество')
    image = forms.ImageField(label='Изображение', required=False)


class ImageForm(forms.Form):
    image = forms.ImageField()
