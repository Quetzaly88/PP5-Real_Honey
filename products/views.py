from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product, ProductSize, ProductSizeFormSet
from django.core.paginator import Paginator
from django.db.models import Q, F, Min, Max
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse


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


@login_required
def add_product(request):
    """Add a product to the store and its sizes"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        formset = ProductSizeFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            product = form.save()
            sizes = formset.save(commit=False)
            for size in sizes:
                size.product = product
                size.save()
            messages.success(request, f"Product '{product.name}' added successfully!")
            return redirect('product_list')
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        formset = ProductSizeFormSet(queryset=ProductSize.objects.none())

    template = 'products/add_product.html'
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, template, context)

    # if request.method == 'POST':
    #     form = ProductForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         product = form.save()
    #         messages.success(request, f"Product '{product.name}' added successfully!")
    #         return redirect('product_list')
    #     else:
    #         messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    # else:
    #     form = ProductForm()

    # template = 'products/add_product.html'
    # context = {'form': form}
    # return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit an existing product"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing: {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f"Product '{product.name}' deleted successfully!")
    return redirect('product_list')
