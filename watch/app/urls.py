from django.urls import path
from . import views
urlpatterns=[
    path('',views.shp_login),
    path('shp_login1/', views.shp_login1, name='shp_login1'),
    path('shp_logout',views.shp_logout),


    # ---------------shop--------------------


    path('shp_home',views.shp_home),
    path('add_prod',views.add_prod),
    path('edit_prod/<pid>',views.edit_prod),
    path('delete_prod/<pid>',views.delete_prod),


    # --------------user---------------------

    path('register/', views.register, name='register'),
    # path('register',views.register),
    # path('user_home',views.user_home),
     path('user_home',views.user_home ,name='user_home'),
    path('view_pro/<pid>',views.view_pro ,name='view_pro'),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart/',views.view_cart),
    path('delete_cart/<id>',views.delete_cart),
    path('user_buy/<cid>',views.user_buy),
    path('user_buy1/<pid>',views.user_buy1),
    path('booking',views.booking),
    path('user_booking',views.user_booking),
    path('order/', views.order, name='order'),
    path('order/success/', views.order_success, name='order_success'),
    path('cancel_buy/<int:buy_id>/', views.cancel_buy, name='cancel_buy'),


    path('product/<int:pid>/', views.view_pro, name='view_product'),
    path('user_buy1/<int:pid>/', views.user_buy1, name='user_buy1'),
   
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/update/<int:id>/<int:quantity>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('cart/delete/<int:id>/', views.delete_cart, name='delete_cart_item'),
    
]



