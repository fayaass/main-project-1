from django.db import models
from django.contrib.auth.models import User



# Create your models here.

# class Product(models.Model):
#     pro_id=models.TextField()
#     name=models.TextField()
#     price=models.IntegerField()
#     ofr_price=models.IntegerField()
#     img=models.FileField()
#     dis=models.TextField()
#     quantity = models.PositiveIntegerField(default=0)  # New field for stock quantity
    

# class Cart(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)


    
#     quantity = models.PositiveIntegerField(default=1)



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    ofr_price = models.FloatField()
    img = models.ImageField(upload_to='products/')
    dis = models.TextField()
    quantity = models.IntegerField(default=0)  # stock quantity
    pro_id = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.ofr_price * self.quantity

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'





# class Buy(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     price=models.IntegerField()
#     date=models.DateTimeField(auto_now_add=True)
#     quantity = models.PositiveIntegerField(default=1)  # Ensure quantity is stored

class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)  # Ensure this field exists
    date = models.DateTimeField(auto_now_add=True)





class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    shipping_address = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)











