from django.shortcuts import render, redirect
from products.models import Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm


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


def product_detail_view(request, **kwargs):
    product = Product.objects.get(id=kwargs['id'])
    if request.method == 'GET':

        context = {
            'product': product,
            'comments': product.review_set.all(),
            'form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product_id=kwargs['id']
            )
            context = {
                'product': product,
                'comment': Review.objects.filter(products_id=kwargs['id']),
                'form': ReviewCreateForm
            }
            return render(request, 'products/detail.html', context=context)


def product_create_view(request):
    if request.method == 'GET':
        data = {
            'form': ProductCreateForm
        }
        return render(request, 'products/products_create.html', context=data)

    else:
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                # image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate')
            )

            return redirect('/products')
        else:
            data = {
                'form': form
            }

        return render(request, 'products/products_create.html', context=data)
