from rest_framework import viewsets
from .models import ProductCategory, ProductInventory, Product, CartItem, Users, UserAddress, OrderDetails
from .serializers import (ProductCategorySerializer, ProductInventorySerializer, ProductSerializer,UserLoginSerializer, UserProfileSerializer,
                          CartItemSerializer, UserSerializer, UserAddressSerializer, OrderDetailsSerializer,UserRegistrationSerializer,ProductResponse)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'registration success'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token, 'msg': 'Login success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non-field_errors':['Email or password is not valid']}},
                                status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):   # it will return user info and address info
    permission_classes = [IsAuthenticated]
    def get(self,request, format=None):
        user = request.user
        try:
            user_address = UserAddress.objects.get(user=user)
        except UserAddress.DoesNotExist:
            user_address = None

        user_data ={
            'id':user.id,
            'email':user.email,
            "name": user.name,
            "tc": user.tc,
            "address": user_address
        }
        serializer = UserProfileSerializer(user_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

def productById(request,cat_id):
    products = Product.objects.filter(category_id=cat_id)
    serializer = ProductResponse(products,many=True)
    return JsonResponse(serializer.data, safe=False)

class ProductInventoryViewSet(viewsets.ModelViewSet):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UserAddressView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        try:
            user_address = UserAddress.objects.get(user=request.user)
            serializer = UserAddressSerializer(user_address, data=request.data,partial=True)
            message = "Address Updated"
        except UserAddress.DoesNotExist:
            serializer = UserAddressSerializer(data=request.data)
            message = "Address Created"

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({"msg": message, "address":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailsViewSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer
