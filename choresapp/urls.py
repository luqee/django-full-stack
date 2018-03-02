from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client_register', views.client_register, name='cli_register'),
    path('provider_register', views.provider_register, name='prov_register'),
    path('client_home', views.client_home, name='cli_home'),
    path('provider_home', views.provider_home, name='pro_home'),
    path('trans_detail/<int:trans_id>', views.trans_detail, name='trans_detail'),
    
]
