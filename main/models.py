from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField()
    image = models.ImageField(upload_to="")


    def __str__(self):
        return self.name
    