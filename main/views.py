from django.shortcuts import render
from django.http import HttpResponse


def get_main_page(request):
    return HttpResponse('Hi')
