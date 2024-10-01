from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
     return self.name    
    

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.brand} {self.model} "
