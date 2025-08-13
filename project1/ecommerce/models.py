from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User,Group

# Create your models here.

# Category Models 

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.TextField()

    def __str__(self):
        return f"{self.category_name}"

# Vendor Models

class Vendor(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.TextField()
    username=models.CharField(max_length=30)
    vendor_email = models.CharField()
    vendor_city = models.CharField()
    vendor_phone = models.CharField(max_length=12)
    vendor_password = models.CharField(max_length=25)
    vendor_address = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.vendor_name}"
    
# Product Models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.TextField()
    product_description = models.CharField(max_length=800)
    product_price = models.DecimalField(max_digits=20,decimal_places=2)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    vendor_id = models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='productimages/',blank=True,null=True)

    def __str__(self):
        return f"{self.product_name}"
      
# Customer Models

class Customer(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    username=models.CharField(max_length=30)
    customer_city = models.TextField()
    customer_email = models.CharField(max_length=50)
    customer_password = models.CharField(max_length=25)
    customer_address =  models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer_name} from {self.customer_city}"
    
    
# Product Models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.TextField()
    product_description = models.CharField(max_length=800)
    product_price = models.DecimalField(max_digits=20,decimal_places=2)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    vendor_id = models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='productimages/',blank=True,null=True)

    def __str__(self):
        return f"{self.product_name}"
    
    
# Order Models

class Order(models.Model):
    order_id =  models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    order_date = models.DateField(auto_now_add=True)
    order_status = models.CharField(max_length=50)
    total_amount =  models.DecimalField(max_digits=20,decimal_places=2)

    def __str__(self):
        return f"{self.order_id} has been ordered on {self.order_date}"
    
#  Order details Models

class Odetail(models.Model):
    odetail_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.odetail_id} has been added in DB "
    
# Payment Models 

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=20)
    payment_amount = models.DecimalField(max_digits=20,decimal_places=2)

# Shipping Models

class shipping(models.Model):
    ship_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    ship_address =  models.CharField(max_length=100)
    ship_date = models.DateField(auto_now_add=True)
    ship_staus = models.TextField()

    def __str__(self):
        return f"{self.ship_id} is shipped to {self.ship_address}"
    
# Review Models 

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    rating = models.CharField(max_length=10)
    comment = models.CharField(max_length=100)