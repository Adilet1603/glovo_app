from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

router = routers.SimpleRouter()


router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'cart', CartViewSet, basename='carts')
router.register(r'cart_item', CartItemViewSet, basename='cart_items')
router.register(r'order', OrderViewSet, basename='orders')
router.register(r'courier', CourierViewSet, basename='couriers')
router.register(r'courier_rating', CourierRatingViewSet, basename='courier_ratings')
router.register(r'combo', ComboViewSet, basename='combos')
router.register(r'contact', ContactViewSet, basename='contacts')




urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreListAPIView.as_view(), name= 'store_list'),
    path('store/<int:pk>/', StoreDetailAPIView.as_view(), name= 'store_detail'),
    path('store/create/', StoreCreateAPIView.as_view(), name= 'store_create'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('store_list/', StoreListOwnerAPIView.as_view(), name = 'store_list_owner'),
    path('store_list/<int:pk>/', StoreDetailUpdateDestroyOwnerAPIView.as_view(), name= 'store_list_edit'),
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductUpdateDestroyOwnerAPIView.as_view(), name='product_update_delete'),
    path('product/create/', ProductCreateAPIView.as_view(), name= 'product_create'),
    path('review/', StoreReviewAPIView.as_view(), name = 'review_create'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



