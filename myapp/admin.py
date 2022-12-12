
from myapp.models import Product
from django.contrib import admin
from . models import Cart

# Register your models here.

# admin.site.register(Product)



admin.site.site_header = 'Mysite Cart Administration'
admin.site.site_title = 'Mysite'
admin.site.index_title = 'Mysite Cart'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','id','price','description')
    search_fields = ('name',)
    
    
    def set_price_to_zero(self,request,queryset):
        queryset.Update(price=0)
    
    def set_price_to_fiftyk(self,request,queryset):
        queryset.Update(price=50000)
        
    actions = ('set_price_to_zero','set_price_to_fiftyk',)
    
admin.site.register(Product,ProductAdmin)


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display =['name','id','price','description']