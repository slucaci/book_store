from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Review(models.Model):
    """ A model to define the review details """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.user.username}'s review of {self.product.name}"

