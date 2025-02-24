from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator
from django.db.models import Q


# Handles displaying and filtering the product list based on filters
def product_list(request, category=None):
    search_query = request.GET.get('search', '')
    size_filter = request.GET.get('size', [])
    price_min = request.GET.get('price_min', None)
    price_max = request.GET.get('price_max', None)
    sort_by = request.GET.get('sort_by', 'name')

    products = Product.objects.all()

    if category:
        products = products.filter(category=category)

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    if size_filter:
        products = products.filter(
            product_sizes__size__in=size_filter).distinct()

    if price_min:
        products = products.filter(product_sizes__price__gte=price_min)

    if price_max:
        products = products.filter(product_sizes__price__lte=price_max)

    products = products.order_by(sort_by)

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {
        'products': page_obj,
        'sort_by': sort_by,
        'search_query': search_query,
        'size_filter': size_filter,
        'price_min': price_min,
        'price_max': price_max,
        'category': category,
        'request': request
    })


def product_detail(request, pk):
    product = get_object_or_404(
        Product.objects.prefetch_related('product_sizes'), pk=pk)
    return render(request, 'products/product_detail.html', {
        'product': product
    })
