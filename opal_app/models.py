from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OpalProduct(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=750, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)    
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

class OpalCollection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=750, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)    
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.title)

class GemStone(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=750, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)    
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.title)

class ExportedOpal(models.Model):
    title = models.CharField(max_length=200)
    site = models.CharField(max_length=200)
    exported_to = models.CharField(max_length=200)
    description = models.TextField(max_length=750, null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)    
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.title)

class Message(models.Model):
    email = models.EmailField(max_length=120)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)
