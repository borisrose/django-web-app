from django.contrib import admin

# Register your models here.

from inventory.models import Seller
from inventory.models import Inventory

class SellerAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname')

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('title',)



admin.site.register(Seller, SellerAdmin)
admin.site.register(Inventory, InventoryAdmin)