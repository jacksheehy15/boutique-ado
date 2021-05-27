<<<<<<< HEAD
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
=======
from django.shortcuts import render, redirect, reverse, HttpResponse
>>>>>>> 5dc7bd346f33bb77d3fff5ded7b9b3ec79c5b32e
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

<<<<<<< HEAD
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
=======

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
>>>>>>> 5dc7bd346f33bb77d3fff5ded7b9b3ec79c5b32e
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
<<<<<<< HEAD
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
=======
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
>>>>>>> 5dc7bd346f33bb77d3fff5ded7b9b3ec79c5b32e
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
<<<<<<< HEAD
    
=======

>>>>>>> 5dc7bd346f33bb77d3fff5ded7b9b3ec79c5b32e

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

<<<<<<< HEAD
    product = get_object_or_404(Product, pk=item_id)
=======
>>>>>>> 5dc7bd346f33bb77d3fff5ded7b9b3ec79c5b32e
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
<<<<<<< HEAD
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
=======
>>>>>>> 5dc7bd346f33bb77d3fff5ded7b9b3ec79c5b32e
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
<<<<<<< HEAD
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
=======
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
>>>>>>> 5dc7bd346f33bb77d3fff5ded7b9b3ec79c5b32e

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
<<<<<<< HEAD
        product = get_object_or_404(Product, pk=item_id)
=======
>>>>>>> 5dc7bd346f33bb77d3fff5ded7b9b3ec79c5b32e
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
<<<<<<< HEAD
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
=======
        else:
            bag.pop(item_id)
>>>>>>> 5dc7bd346f33bb77d3fff5ded7b9b3ec79c5b32e

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
<<<<<<< HEAD
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
=======
        return HttpResponse(status=500)
>>>>>>> 5dc7bd346f33bb77d3fff5ded7b9b3ec79c5b32e
