from django.urls import path
from .views import (
    HomeView,
    OrderSummaryView,
    CheckoutView, 
    ItemDetailView, 
    add_to_cart,
    remove_from_cart, 
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    profile,
    update_profile,
    ChangePasswordView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-form-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),    
    path('profile/', profile, name='user-profile'),
    path('update-profile/', update_profile, name='update-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]