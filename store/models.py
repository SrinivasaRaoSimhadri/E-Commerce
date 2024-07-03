from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product_id = models.IntegerField(null=False)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    quantity_price = models.FloatField(default=0)
    image = models.URLField(default='https://example.com/default_image.jpg')
    # payment_status = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user} {self.product_id}'

    
    
class Address(models.Model):
    user = models.OneToOneField(User , max_length=30 , on_delete=models.CASCADE)
    name = models.CharField(max_length= 30 ,null=False)
    email = models.CharField(max_length= 30 ,null=False)
    Address = models.TextField()
    city = models.CharField(max_length= 30)
    state = models.CharField(max_length= 30 ,null=False)
    zipcode = models.CharField(max_length= 30 ,null=False , blank=False)

class Payment(models.Model):
    user = models.ForeignKey(Cart , on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)
    # order_id , amount 