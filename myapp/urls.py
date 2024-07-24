from django.urls import path, include
from myapp.views import UserRegistrationView,UserLoginView,UserProfileView, UserAddressView,productById
urlpatterns = [
    path("register/",UserRegistrationView.as_view(),name='register'),
    path("login/", UserLoginView.as_view(), name='login'),
    path("profile/", UserProfileView.as_view(), name='profile'),
    path("user-address/", UserAddressView.as_view(), name='user-address'),
    path("productByCategory/<int:cat_id>",productById),
]
