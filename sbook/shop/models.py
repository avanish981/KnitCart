from django.db import models
from shop.forms import User

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    user=models.ForeignKey(User,on_delete="CASCADE",null=True,default=0)
    product_name = models.CharField(max_length=50,default="")
    category = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    price1=models.CharField(max_length=50,default=0)
    desc = models.CharField(max_length=300,default="")
    image = models.ImageField(upload_to='shop/images', default="")
    phone = models.CharField(max_length=70, default="")

    class Meta:
         db_table="Product"

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    class Meta:
        db_table="Contact"


    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    room_no=models.CharField(max_length=111,default="")
    year=models.CharField(max_length=111,default="")
    phone = models.CharField(max_length=111, default="")
    product_name=models.CharField(max_length=100,default="")
    class Meta:
        db_table="Order"
class Signup(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    class Meta:
        db_table="UserProfileInfo"
    def __str__(self):
        return self.username
class First(models.Model):
    usernmae=models.CharField(max_length=100)
    class First:
        db_table="First"
