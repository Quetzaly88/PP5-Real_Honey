from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def product_list(request):
    sort_by = request.GET.get('sort_by', 'name') # default sort by name
    products = Product.objects.all().order_by(sort_by)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'products/product_list.html', {'page_obj': page_obj})