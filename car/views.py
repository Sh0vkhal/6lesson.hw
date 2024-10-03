from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from .models import Brand,Color,Car
from .serializers import CarSerializer,BrandSerializer,ColorSerializer



class CarAPIViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
