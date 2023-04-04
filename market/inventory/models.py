from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


#first model
class Seller(models.Model):

    def __str__(self): 
        return f'{self.lastname}'

    firstname = models.fields.CharField(max_length=15, null=True)
    lastname = models.fields.CharField(max_length=20, null=True)
    email = models.fields.CharField(max_length=15, null=True)
    password = models.fields.CharField(max_length=20, null=True)
    address = models.fields.CharField(max_length=15, null=True)


#second mondel
class Inventory(models.Model):

    seller = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)  
    title = models.fields.CharField(max_length=15, null=True)
    description = models.fields.CharField(max_length=300, null=True)
    is_sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True);
    image_url = models.fields.URLField(null=True, blank=True)
