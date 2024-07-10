from rest_framework import serializers
from myapp import models as model_file

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'})
    class Meta:
        model = model_file.Users
        fields = ['email','name','password','password2','tc']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    #validating password
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password1 and 2 did't match")
        return attrs

    def create(self, validated_data):
        return model_file.Users.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    class Meta:
        model = model_file.Users
        fields = ["email","password"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = model_file.Users
        fields = ["id", "email", "name"]

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
