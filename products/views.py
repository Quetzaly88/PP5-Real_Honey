from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def product_list(request):
    sort_by = request.GET.get('sort_by', 'name')
    products = Product.objects.all().order_by(sort_by)  
    
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'products/product_list.html', {'products': page_obj, 'sort_by': sort_by})

def product_detail(request, pk): #Function parameter is called pk
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

