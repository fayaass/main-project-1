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
    path('view_pro/<pid>',views.view_pro),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart/',views.view_cart),
    path('delete_cart/<id>',views.delete_cart),
    path('user_buy/<cid>',views.user_buy),
    path('user_buy1/<pid>',views.user_buy1),
    path('booking',views.booking),
    path('user_booking',views.user_booking),
    path('order/', views.order, name='order'),
    path('order/success/', views.order_success, name='order_success'),

    
]



