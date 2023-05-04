from django import forms
from products.models import Product

PRODUCT_CHOISES = (
    (product.id, product.title) for product in Product.objects.all()
)


class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=3)
    # image = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea, min_length=3)
    rate = forms.IntegerField()


class ReviewCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, min_length=3, label="оставить отзыв:")
    product = forms.ChoiceField(choices=PRODUCT_CHOISES)
