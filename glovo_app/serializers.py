from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'status']


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']


class CategorySimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name',]

class ComboSerializers(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = '__all__'

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['title', 'contact_number', 'social_network']

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CourierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'



class CourierRatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourierRating
        fields = '__all__'


class StoreListSerializers(serializers.ModelSerializer):
    category = CategorySimpleSerializers()

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'category', 'store_image']


class StoreDetailSerializers(serializers.ModelSerializer):
    category = CategorySimpleSerializers()
    owner = UserProfileSimpleSerializers()
    contacts = ContactSerializers(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ['store_name', 'category', 'store_image',
                  'description', 'address', 'contacts','owner']



class StoreSerializers(serializers.ModelSerializer):
    model = Store
    fields = '__all__'


class CategoryDetailSerializers(serializers.ModelSerializer):
    store_list = StoreListSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'store_list']


class StoreReviewSimpleSerializers(serializers.ModelSerializer):
    # client = UserProfileClientSerializer()
    # created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    #
    class Meta:
        model = StoreReview
        fields = '__all__'

class StoreReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = StoreReview
        fields = '__all__'



class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'





# product
# order
# store
# storereview
# courier
# courierrating
# cart
# cartitem
# user
# category
# combo
# contact

