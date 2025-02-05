from django.contrib import admin

from .models import *


from .models import Product, Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)



