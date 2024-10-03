from django.urls import path
from rest_framework import routers
from .views import CarAPIViewSet,BrandViewSet,ColorViewSet




router = routers.DefaultRouter()
router.register(r'car', CarAPIViewSet,basename='car')
router.register(r'brand',BrandViewSet,basename='brand')
router.register(r'color',ColorViewSet,basename='color')
urlpatterns = router.urls