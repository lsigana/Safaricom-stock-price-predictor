from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_data_view, name='stock_data'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]
