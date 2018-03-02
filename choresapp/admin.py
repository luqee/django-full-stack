from django.contrib import admin

# Register your models here.

from .models import Client, Provider, Transaction, Category

admin.site.register(Client)
admin.site.register(Provider)
admin.site.register(Transaction)
admin.site.register(Category)
