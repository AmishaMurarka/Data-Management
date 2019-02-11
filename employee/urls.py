from django.urls import path, include
from . import views

urlpatterns=[

#	path('mainpage/', views.mainpage, name='mainpage'),
	path('main/', views.Page.loginpage, name='loginpage'),
	path('main/orders/', views.Page.orderspage, name='orderspage'),
	path('main/customers', views.Page.customerpage, name='customerpage'),
	path('main/products', views.Page.productpage, name='productpage'),
        path('main/calendar',views.Page.calendarpage,name='calendarpage'),
	path('main/logout',views.Page.logoutpage,name='logoutpage'),
]
