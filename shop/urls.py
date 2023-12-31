from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "shop"
urlpatterns = [
    path('',views.index, name = "index"),
    path('login/',views.logIn, name = "login"),
    path('signup/',views.signup, name = "signup"),
    path('about/',views.about, name = "about"),
    path('contact/',views.contact, name = "contact"),
    path('cart/',views.cart, name = "cart"),
    path('account/<str:username>',views.account, name = "account"),
    path('checkout/',views.checkout, name = "checkout"),
    path('product/<int:product_id>',views.product, name = "product"),
    path('categories/<int:category_id>',views.categories, name = "categories"),
    path('addFromProduct/<int:productId>',views.addFromProduct, name = "addFromProduct"),
    path('setcart/',views.setcart, name = "setcart"),
    path('signout/',views.logOut, name = "signout"),
    path('order/',views.order, name = "order"),
    path('orders/',views.myOrders, name = "orders"),
    path('message/',views.message, name = "message"),
    

]

    
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)