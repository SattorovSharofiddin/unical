from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from mptt.admin import DraggableMPTTAdmin

from .models import Shop, Product, Category


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title',)
    list_display_links = ('indented_title',)
    search_fields = ('title', 'id', 'parent__title')
    # prepopulated_fields = {'slug': ('title',)}


class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_url')
    search_fields = ('title',)
    inlines = [ProductInline]


class ProductAdmin(admin.ModelAdmin, DynamicArrayMixin):
    exclude = ('id',)
    # list_display = ('title', 'description', 'price', 'active', 'main_image')
    search_fields = ('title', 'id')

    # list_filter = ('active', 'price')

    def main_image(self, obj):
        return '<img src="{}" height="50" />'.format(obj.image)

    main_image.allow_tags = True
    main_image.short_description = 'Main Image'


admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
