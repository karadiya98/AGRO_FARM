from django.urls import path
from .views import home, second,first,login,carts,orders,detail,account,datainserted,login_view,profile,logout_view,add_cart_backened,payment,add_order_backened,remove_item_cart,cancelled_item_order,chart,bill

urlpatterns = [
    path('', first, name='first'),
    path('loginuser.html',login,name='second'),
    path('login_view',login_view,name='login_view'),
    path('home.html', home, name='home'),
    path('acccountuser.html', account, name='account'),
    path('carts.html', carts, name='carts'),
    path('order.html', orders, name='order'),
    path('Detail_product.html', detail, name='detail'),
    path('datainserted',datainserted, name='datainserted'),
    path('profile.html/',profile, name='profile'),
    path('logout/',logout_view, name='logout'),
    path('cartinserted/',add_cart_backened, name='cartinserted'),
    path('payment.html',payment, name='payment'),
    path('orderinserted/',add_order_backened, name='orderinserted'),
   path('removed/',remove_item_cart, name='remove_item_cart'), # Corrected URL pattern
   path('cancelled/',cancelled_item_order, name='cancelled_item_order'),
   path('charts',chart, name='chart'),
   path('bill',bill, name='bill'),
]
