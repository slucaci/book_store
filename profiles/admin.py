from django.contrib import admin
from .models import UserProfile, Wishlist

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product') 
    search_fields = ('user__username', 'product__name') 
    list_filter = ('user',)

admin.site.register(UserProfile) 
admin.site.register(Wishlist, WishlistAdmin) 