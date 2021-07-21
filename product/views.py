from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    product = Product.objects.all()
    paginator = Paginator(product, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'home.html', {'product':page})

def detail(request, id):
    product = get_object_or_404(Product, pk = id)
    return render(request, 'detail.html', {'product':product})

def make_post(request):
    if request.method == "POST":
        new_product = Product()
        new_product.pdname = request.POST['pdname']
        new_product.pdprice = request.POST['pdprice']
        new_product.pdbody = request.POST['pdbody']
        new_product.pdimage = request.FILES['pdimage']
        new_product.save()
        return redirect('home')
    else:
        return render(request, 'new.html')

def edit(request, id):
    if request.method == "POST":
        edit_product = Product.objects.get(id = id)
        edit_product.pdname = request.POST['pdname']
        edit_product.pdprice = request.POST['pdprice']
        edit_product.pdbody = request.POST['pdbody']
        edit_product.pdimage = request.FILES['pdimage']
        edit_product.save()
        return redirect('detail', edit_product.id)
    else:
        product = Product.objects.get(id = id)
        return render(request, 'edit.html', {'product':product})

def delete(request, id):
    delete_product = Product.objects.get(id = id)
    delete_product.delete()
    return redirect('home')
