from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Consumer)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Transactions)


# Registering models in django admin
# username: admin, pasword: admin