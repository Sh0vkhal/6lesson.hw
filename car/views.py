from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated

# Create your views here.
from .models import Brand,Color,Car
from .serializers import BrandSerializer,ColorSerializer,CarSerializer


class CarAPIView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CarsAPIView(RetrieveUpdateDestroyAPIView):   
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


class BrandAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BrandsAPIView(RetrieveUpdateDestroyAPIView):   
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]


class ColorAPIView(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
