from django.shortcuts import render

def primary(requests):
    return render(requests, 'base.html')
