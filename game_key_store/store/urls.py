from django.urls import path
from . import views
#Пути
urlpatterns = [
    path('api/categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('api/products/', views.ProductListAPIView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
]