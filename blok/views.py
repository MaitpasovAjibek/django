from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Product,Category

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
    product = Product.objects.all()
    context = {
        'product':product,
        'title':'список постов'

    }

    if request.method == 'GET':
        return render(request, 'blok/products.html',context=context )


def category_view(request):
    category = Category.objects.all()
    cont = {
        'category':category
    }
    if request.method == 'GET':
        return render(request,'blok/categories.html',context=cont)