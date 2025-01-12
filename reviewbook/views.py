from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Review


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment", "")

        if not rating:
            messages.error(request, "Rating is required.")
            return redirect("product_detail", product_id=product.id)

        review, created = Review.objects.update_or_create(
            product=product, user=request.user,
            defaults={"rating": rating, "comment": comment}
        )
        messages.success(request, "Your review has been submitted.")
        return redirect("product_detail", product_id=product.id)

    return render(request, "reviewbook/add_review.html", {"product": product})
