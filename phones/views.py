from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones_all = Phone.objects.all()
    sort_by = request.GET.get('sort', None)
    if sort_by:
        if sort_by == 'name':
            phones_all = phones_all.order_by('name')
        elif sort_by == 'min_price':
            phones_all = phones_all.order_by('price')
        elif sort_by == 'max_price':
            phones_all = phones_all.order_by('-price')
    template = 'catalog.html'
    context = {'phones': phones_all}
    return render(request, template, context)


def show_product(request, slug):
    # Используем get_object_or_404 для получения объекта Phone по slug
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)

