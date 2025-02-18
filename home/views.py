from django.shortcuts import render
from products.models import Product


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def home_view(request):
    featured_products = Product.objects.order_by('?')[:3]
    return render(request, 'home/home.html', {
        'featured_products': featured_products})
