from django.contrib import admin
from .models import UserProfile, Wishlist
from .models import LoyaltyPoints

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product') 
    search_fields = ('user__username', 'product__name') 
    list_filter = ('user',)

admin.site.register(UserProfile) 
admin.site.register(Wishlist, WishlistAdmin) 
admin.site.register(LoyaltyPoints)