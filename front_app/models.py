from turtle import position, title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Catagory(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.title)

class Message(models.Model):
    sender = models.ForeignKey( User,on_delete=models.SET_NULL, null=True)
    email = models.EmailField(max_length=120)
    subject = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.subject)

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.subject)

class Promotion(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='promotion_video', null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.title)

class Sponser(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.title)

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=750, null=True, blank=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True)
    icon = models.ImageField(null=True, blank=True)    
    price = models.DecimalField(max_digits=7, decimal_places=2)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=250)
    relase_date = models.DateTimeField(auto_now_add=True)
    tip = models.TextField(null=True, blank=True)  

    def __str__(self) -> str:
        return str(self.title)

class ProductImage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True) 

    def __str__(self) -> str:
        return str(self.title)

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True) 
    icon_class = models.CharField(max_length=200, null=True, blank=True)
    icon_class2 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.title)

class Testimonial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_name = models.CharField(max_length=200, default='Unknown')
    user_position = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.title)

class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.position +' : '+ self.user.username)