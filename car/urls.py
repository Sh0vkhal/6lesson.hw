from django.urls import path
from .views import CarAPIView,CarsAPIView,BrandAPIView,BrandsAPIView,ColorAPIView



urlpatterns = [
    path('',CarAPIView.as_view()),
    path('car/<int:pk>/', CarsAPIView.as_view()),
    path('brand/', BrandAPIView.as_view()),
    path('brand/search/<int:pk>/', BrandsAPIView.as_view()),
    path('color/', ColorAPIView.as_view()),
]
