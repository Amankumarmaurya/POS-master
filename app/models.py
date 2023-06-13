from django.db import models

# Create your models here.
class Inventory(models.Model):
    inventoryname=models.CharField(max_length=100)
    quantity=models.IntegerField()
    sellingprice=models.IntegerField()
    costprice=models.IntegerField()
    category=models.CharField(max_length=50)
    subcategory=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)

    def __str__(self):
        return str(self.inventoryname)
class delivery(models.Model):
    staffname=models.CharField(max_length=100)
    product=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    price=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=100)

    def __str__(self):
        return str(self.delivery)
    
class Customer(models.Model):
    customername=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    product=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    def __str__(self):
        return str(self.customername)


class Staff(models.Model):
    staffname=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    salary=models.CharField(max_length=100)
    def __str__(self):
        return str(self.staffname)

class Product(models.Model):
    productname=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    subcategory=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    productcode=models.CharField(max_length=50)
    def __str__(self):
        return str(self.productname)

class POS(models.Model):
    customername=models.CharField(max_length=100)
    product=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    sellingprice=models.IntegerField()
    quantity=models.IntegerField()
    def __str__(self):
        return str(self.customername)


