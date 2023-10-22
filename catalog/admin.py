from django.contrib import admin

from catalog.models import Product, Category, Contacts


@admin.register(Product)
class AutocarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class MarkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(Contacts)