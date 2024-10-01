from rest_framework import serializers

from .models import Brand,Color,Car

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Car
        fields = "__all__"
            