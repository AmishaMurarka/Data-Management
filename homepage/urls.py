from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns =  [

	path('', LoginView.as_view(template_name= 'homepage/login.html'), name='login'),
	path('employee/', include('employee.urls')),
	path('admin/', include('manager.urls')),

]
