from django.shortcuts import get_object_or_404, render
from .models import Product
# Create your views here.


def all_products(request):
    """
    A view to all products inclduing sorting and searching
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request,'products/products.html', context)


def product_detail(request, product_id):
    """
    Individual product information
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request,'products/product_detail.html', context)
