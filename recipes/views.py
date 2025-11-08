from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def contacts(request):
    return HttpResponse('Contatos')


def home(request):
    return HttpResponse('Home')


def about(request):
    return HttpResponse('Sobre')
