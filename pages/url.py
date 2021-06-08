from django.urls import path
from . import views
urlpatterns = [
    path('', views.test),
    path('product_pc/', views.product, name='product'),
    path('registration/', views.registration, name='registration'),
    path('sing-up/', views.sing_up, name='sing-up'),
]
