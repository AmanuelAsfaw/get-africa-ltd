from django.contrib import admin

from front_app.models import Catagory, Message, Product, ProductImage, Promotion, Response, Service, Sponser, Testimonial

# Register your models here.

admin.site.register(Catagory)
admin.site.register(Message)
admin.site.register(Response)
admin.site.register(Promotion)
admin.site.register(Sponser)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Service)
admin.site.register(Testimonial)