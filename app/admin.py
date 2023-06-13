from django.contrib import admin

from app.models import Inventory,Customer,Staff,Product,POS, delivery

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Product)
admin.site.register(POS)
admin.site.register(delivery)