from django.shortcuts import render
from products.models import Product


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def home_view(request):
    featured_products = Product.objects.filter(
        is_featured=True).order_by('?')[:3]
    best_seller_products = Product.objects.filter(
        is_bestseller=True).order_by('?')[:3]

    return render(request, 'home/index.html', {
        'featured_products': featured_products,
        'best_seller_products': best_seller_products,
    })
