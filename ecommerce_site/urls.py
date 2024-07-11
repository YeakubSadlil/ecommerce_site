
from django.contrib import admin
from django.urls import path, include
from myapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product-categories', views.ProductCategoryViewSet)
router.register('product-inventories', views.ProductInventoryViewSet)
router.register('products', views.ProductViewSet)
router.register('cart-items', views.CartItemViewSet)
router.register('users', views.UserViewSet)
# router.register('user-address', views.UserAddressViewSet)
router.register('order-details', views.OrderDetailsViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include(router.urls)),
    path("api/user/",include('myapp.urls'))
]
