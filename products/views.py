from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator
from django.db.models import Q, F, Min, Max


# Handles displaying and filtering the product list based on filters
def product_list(request, category=None):
    search_query = request.GET.get('search', '')
    size_filter = request.GET.get('size', '')
    price_min = request.GET.get('price_min', None)
    price_max = request.GET.get('price_max', None)
    sort_by = request.GET.get('sort_by', 'name')

    products = Product.objects.all().prefetch_related('product_sizes')

    #  Filter by category if provided
    if category:
        products = products.filter(category=category)

    # search filter
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # size filter
    if size_filter:
        if size_filter == 'Standard':
            products = products.filter(product_sizes__size__in=['', None, 'Standard'])
        else:
            products = products.filter(product_sizes__size=size_filter)

    # price filter
    if price_min:
        try:
            price_min_value = float(price_min)
            products = products.filter(product_sizes__price__gte=price_min_value)
        except (ValueError, TypeError):
            pass

    if price_max:
        try:
            price_max_value = float(price_max)
            products = products.filter(product_sizes__price__lte=price_max_value)
        except (ValueError, TypeError):
            pass

    # removing duplicates
    products = products.distinct()

    # apply sorting
    if sort_by in ['name', 'price']:
        if sort_by == 'price':
            products = products.annotate(min_price=Min('product_sizes__price')).order_by('min_price')
        else:
            products = products.order_by(sort_by)

    # Pagination
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
