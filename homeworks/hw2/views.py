from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product


def index(request):
    return HttpResponse('HOME WORK 2')


def clients(request):
    users = Client.objects.all()
    return HttpResponse(users)


def products(request):
    prs = Product.objects.all()
    return HttpResponse(prs)
