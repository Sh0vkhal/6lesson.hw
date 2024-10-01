from django.contrib import admin

# Register your models here.
from .models import Brand,Color,Car

admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Car)

