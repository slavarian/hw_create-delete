from django.shortcuts import render, redirect

from .forms import CreateForm
from .models import Products

def create_product(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/list') 
    else:
        form = CreateForm()
    
    return render(request, 'add_product.html', {'form': form})

def product_list(request):
    products = Products.objects.all()
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:
            product_to_delete = Products.objects.get(pk=product_id)
            product_to_delete.delete()
            return redirect('product_list')
    
    return render(request, 'list.html', {'products': products})