from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 200,null=True)
    phone = models.CharField(max_length = 200,null=True)
    email = models.CharField(max_length = 200,null=True)
    date_created = models.DateTimeField(null=True,blank = True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
            ('In door','In door'),
            ('Out Door','Out Door'),
    )
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(max_length=200,null=True,blank=True)
    # MANY TO MANY FIELD : 
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
            ('Pending','Pending'),
            ('Out for delivery','Out for delivery'),
            ('Delivered','Delivered'),
    )
    # foreign key : 
    customer = models.ForeignKey(Customer,null=True,on_delete = models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete = models.SET_NULL)

    date_created = models.DateTimeField(max_length=200,null=True,blank=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    note = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.product.name





