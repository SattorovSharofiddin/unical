from django.contrib import admin
from django.utils.safestring import mark_safe
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from mptt.admin import DraggableMPTTAdmin

from .models import Shop, Product, Category, Image


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class PhotoAdmin(admin.StackedInline):
    model = Image
    extra = 0
    min_num = 1


class CategoryAdmin(DraggableMPTTAdmin):
    search_fields = ('title', 'id', 'parent__title')


class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


class ProductAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ('id', 'title', 'main_image', 'amount', 'price', 'active')
    search_fields = ('title', 'id')
    inlines = (PhotoAdmin,)

    def main_image(self, obj):
        return mark_safe(
            f'<a href="http://localhost:8000/admin/app/product/{obj.id}/change/"><img src="{obj.product_images.first().image_url}" height="50" /></a>')

    main_image.allow_tags = True
    main_image.short_description = 'Main Image'


admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
