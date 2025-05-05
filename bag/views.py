from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product
from profiles.models import LoyaltyPoints
from decimal import Decimal
from bag.contexts import bag_contents 


# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    loyalty_points = 0
    if request.user.is_authenticated:
        loyalty, created = LoyaltyPoints.objects.get_or_create(user=request.user)
        loyalty_points = loyalty.points

    return render(request, 'bag/bag.html', {
        'loyalty_points': loyalty_points,
    })
    


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = request.POST.get('quantity', 1)
    try:
        quantity = int(quantity)
    except ValueError:
        quantity = 1 
    redirect_url = request.POST.get('redirect_url', '/')
    if not redirect_url:
        redirect_url = '/' 
    print(f"Redirect URL: {redirect_url}")
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} quantity  to your bag.')
      
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity  to  {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

    
def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    try:
        bag = request.session.get('bag', {})
        if item_id in bag:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

def apply_loyalty_points(request):
    if request.method == "POST":
        user = request.user
        points_to_apply = int(request.POST.get("points_to_apply", 0))
        current_bag = bag_contents(request)
        grand_total = Decimal(current_bag["grand_total"])
        if (grand_total - Decimal(points_to_apply)) < Decimal("5.00"):
            messages.error(request, f"The minimum order total after applying loyalty points must be at least $5.00. You can apply a maximum of {int(grand_total - Decimal('5.00'))} points.")
            return redirect("view_bag")
        if Decimal(points_to_apply) > grand_total:
            messages.error(request, "You cannot apply more points than the order total!")
            print(points_to_apply, grand_total)
            return redirect("view_bag")
        if user.loyalty_points.points >= points_to_apply:
            discount_amount = Decimal(points_to_apply)  
            request.session["loyalty_discount"] = float(discount_amount)
            user.loyalty_points.points -= points_to_apply
            messages.success(request, f"Applied {points_to_apply} points for a discount of ${discount_amount:.2f}")
        else:
            messages.error(request, "Not enough points!")
        

    return redirect("view_bag")