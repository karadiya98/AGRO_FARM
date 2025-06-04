from django.contrib import admin
from .models.products import Products
from .models.category import Categories
from .models.advertisement import advertisement
from .models.delivery import Delivery
from .models.status import Status
from .models.carts import CartItem
from .models.carts1 import CartItem1
from .models.Main_TABLE import Main_table
from .models.User_Detail import User_Detail


class admintable(admin.ModelAdmin):
    list_display=['id','name','description','category','price']

  
class maintable(admin.ModelAdmin):
    list_display = ['order_id', 'user_name', 'product_name', 'price_per_item','quantity', 'total_amount']
    
class userdetail(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'gmail', 'password', 'confirm_password']
       
class carttable(admin.ModelAdmin):
    list_display = ['productid', 'userid', 'name','quantity' , 'price', 'image']
       


admin.site.register(Products,admintable)
admin.site.register(Categories)
admin.site.register(advertisement)
admin.site.register(Delivery)
admin.site.register(Status)
admin.site.register(CartItem,carttable)
admin.site.register(Main_table,maintable)
admin.site.register(User_Detail,userdetail)