from rest_framework import serializers
from myapp import models as model_file

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = model_file.ProductCategory
        fields = '__all__'
class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = model_file.ProductInventory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = model_file.Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = model_file.CartItem
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = model_file.Users
        fields = '__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = model_file.UserAddress
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = model_file.OrderDetails
        fields = '__all__'
