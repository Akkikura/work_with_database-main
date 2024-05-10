from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones_all = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones_all}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug__contains=slug).all()

    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
