from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('log', views.register_page, name='log'),
    path('register_user', views.register, name='register_user'),
    path('login', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
    path('logout', views.logout, name='logout'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('sale_invoices', views.sale_invoices, name='sale_invoices'),
    path('estimate_quotation', views.estimate_quotation, name='estimate_quotation'),
    path('payment_in', views.payment_in, name='payment_in'),
    path('sale_order', views.sale_order, name='sale_order'),
    path('delivery_chellan', views.delivery_chellan, name='delivery_chellan'),
    path('sale_return_cr', views.sale_return_cr, name='sale_return_cr'),
    
]
