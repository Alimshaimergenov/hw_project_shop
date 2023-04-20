from django.shortcuts import render
from products.models import Product


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        contex = {
            'product': product
        }

        return render(request, 'products/detail.html', context=contex)
