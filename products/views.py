from django.shortcuts import render, redirect
from products.models import Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm
from .constants import PAGINATION_LIMIT


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        if search_text:
            products = products.filter(title__icontains=search_text)
        max_page = round(products.__len__() / PAGINATION_LIMIT)
        products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'max_page': range(1, max_page + 1)
        }
        return render(request, 'products/products.html', context=context)


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def product_detail_view(request, id, **kwargs):
    product = Product.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'product': product,
            'comments': product.review_set.all(),
            'form': ReviewCreateForm,
            'user': request.user
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product_id=id
            )
            context = {
                'product': product,
                'comment': Review.objects.filter(product_id=id),
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
