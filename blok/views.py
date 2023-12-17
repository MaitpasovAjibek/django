from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def main_view(request):
    if request.method == 'GET':
        return render(request, 'blok/index.html')

def current_date_view(request):
    if request.method == 'GET':
        now = datetime.now()
        return HttpResponse(now.strftime('%Y-%m-%d'))


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('GoodBye my friend/user')


def product_view(request):
    if request.method == 'GET':
        return render(request, 'blok/products.html')