from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_country = models.CharField(default='IE',max_length=40, null=False, blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        LoyaltyPoints.objects.create(user=instance)
    else:
        # Existing users: just save the profile
        instance.userprofile.save()
        instance.loyalty_points.save()


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlisted_by")

    class Meta:
        unique_together = ('user', 'product') 

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

class LoyaltyPoints(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="loyalty_points")
    points = models.IntegerField(default=0)
    redeemed_points = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def available_points(self):
        """ Calculate points available for use """
        return self.points - self.redeemed_points

    def __str__(self):
        return f"{self.user.username} - {self.available_points()} points"