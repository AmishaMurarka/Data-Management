from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns=[

    path('main/', views.Page.admin_login, name='admin_login'),
    path('main/orders/', views.Page.orderspage, name='adminorderspage'),
    path('main/customers', views.Page.customerpage, name='admincustomerpage'),
    path('main/products', views.Page.productpage, name='adminproductpage'),
    path('main/calendar',views.Page.calendarpage,name='admincalendarpage'),
    path('main/contact',views.Page.contactpage,name='contactpage'),
    path('main/logout',views.Page.logoutpage,name='logoutpage'),
    path('main/download_order',views.Page.downloadorder,name='downloadorder'),
    path('main/download_customer',views.Page.downloadcustomer,name='downloadcustomer'),
    path('main/download_product',views.Page.downloadproduct,name='downloadproduct'),
    
]
