from django.template.context_processors import request

from .serializers import *
from .models import *
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import CheckOwner, CheckUserReview, CheckStoreOwner
from rest_framework.authtoken import views
import django_filters

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class ComboViewSet(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializers

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializers


class CourierRatingViewSet(viewsets.ModelViewSet):
    queryset = CourierRating.objects.all()
    serializer_class = CourierRatingSerializers

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['category_name']

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers



class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializers

class StoreListOwnerAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializers

    def get_queryset(self):
        return Store.objects.filter(owner=self.request.user)


class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializers


class StoreReviewAPIView(generics.CreateAPIView):
    serializer_class = StoreReviewSerializers

class StoreCreateAPIView(generics.CreateAPIView):
    serializer_class = StoreSerializers


class StoreDetailUpdateDestroyOwnerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers
    permission_classes = [CheckOwner, CheckStoreOwner]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['product_name']
    ordering_fields = ['price']



class ProductUpdateDestroyOwnerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers