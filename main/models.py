from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextFieldField()
    price = models.DecimalField()
    image = models.ImageField(upload_to="photos")


    def __str__(self):
        return self.name
    