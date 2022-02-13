from django.db import models

# Create your models here.

class Consumer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField()

# Table Consumer with the details of the consumers

class Product(models.Model):
    product_name =  models.CharField(max_length=50)
    price = models.FloatField()

# Table Product with the details of each product

class Orders(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.DO_NOTHING)
    product1 = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, related_name='product1')
    product1_num = models.IntegerField(default=0)
    product2 = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, related_name='product2', blank=True)
    product2_num = models.IntegerField(default=0)
    product3 = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, related_name='product3', blank=True)
    product3_num = models.IntegerField(default=0)
    product4 = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True, related_name='product4', blank=True)
    product4_num = models.IntegerField(default=0)

# Table Orders with the details of every order

class Transactions(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.DO_NOTHING)
    total_order_amount = models.FloatField()
    total_paid_amount = models.FloatField()
    total_pending = models.FloatField()
    transaction_date = models.DateTimeField(auto_now_add=True)

# Table Transactions with the details of each transaction on product purchase
