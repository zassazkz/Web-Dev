from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import fbv, cbv, mixins, generics

router = DefaultRouter()

urlpatterns = [
    # Level 2 - FBV
    path('fbv/products/', fbv.products_list),
    path('fbv/products/<int:product_id>/', fbv.product_detail),

    # Level 3 - CBV
    path('cbv/products/', cbv.ProductListAPIView.as_view()),
    path('cbv/products/<int:product_id>/', cbv.ProductDetailAPIView.as_view()),

    # Level 4 - Mixins
    path('mixins/products/', mixins.ProductListAPIView.as_view()),
    path('mixins/products/<int:product_id>/', mixins.ProductDetailAPIView.as_view()),

    # Level 5 - Generics (main)
    path('products/', generics.ProductListAPIView.as_view()),
    path('products/<int:product_id>/', generics.ProductDetailAPIView.as_view()),
    path('categories/', generics.CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', generics.CategoryDetailAPIView.as_view()),
    path('categories/<int:id>/products/', generics.CategoryProductsAPIView.as_view()),
]