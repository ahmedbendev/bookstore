from django.db import models
from django.contrib.auth.models import User
from store.models import Usedbook
from django.utils import timezone
from django.db.models import Count
from django.urls import reverse
from store.models import Newbook

SHIPPING_CHOICES = (
    ('NORMAL','normal'),
    ('FAST','fast')
)

PAYING_CHOICES = (
    ('CCP','ccp'),
    ('HAND','hand')
)

class Bookorder(models.Model):
    userorderbook = models.ForeignKey(User,on_delete=models.CASCADE)
    newbook = models.ForeignKey(Newbook, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return str(self.pk)
    def get_total_bookorder_price(self):
        return self.quantity * self.newbook.price_book

class Order(models.Model):
    userorder = models.ForeignKey(User , on_delete = models.CASCADE )
    ordered = models.BooleanField(default=False)
    bookorders = models.ManyToManyField(Bookorder)
    orderetat = models.CharField(max_length = 100 , default="waiting for submit")
    order_pub_date = models.DateTimeField(default = timezone.now)
    order_submit_date = models.DateTimeField(null = True,blank = True)
    order_delete_date = models.DateTimeField(null = True,blank = True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    def __str__(self):
        return str(self.pk)
    def get_total(self):
        total = 0
        for bookorder in self.bookorders.all():
            total += bookorder.get_total_bookorder_price()
        return total

class Orderdetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    region_adress = models.CharField(max_length = 256)
    town_adress = models.CharField(max_length = 256)
    city_adress = models.CharField(max_length = 256)
    street_adress = models.CharField(max_length = 256)
    postal_code = models.IntegerField()
    phone_num = models.IntegerField()
    email= models.EmailField()
    shipping_type= models.CharField(choices=SHIPPING_CHOICES,max_length = 100 , default = "normal")
    paying_type= models.CharField(choices=PAYING_CHOICES,max_length = 100 , default = "ccp")
    def __str__(self):
        return str(self.pk)
