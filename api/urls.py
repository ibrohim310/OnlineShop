from django.urls import path
from . import views

urlpatterns = [
    # Category URLs
    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),

    # Product URLs
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),

    # CartItem URLs
    path('cart/', views.cartitem_list, name='cartitem-list'),
    path('cart/<int:pk>/', views.cartitem_detail, name='cartitem-detail'),

    # Order URLs
    path('orders/', views.order_list, name='order-list'),
    path('orders/<int:pk>/', views.order_detail, name='order-detail'),

    # Token Authentication URL
    path('api-token-auth/', views.ObtainAuthToken.as_view(), name='api_token_auth'),
]
