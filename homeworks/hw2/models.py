from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    address = models.CharField(max_length=50, default='vtb')
    date_registration = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Username:{self.name}, email:{self.email} "


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count_product = models.IntegerField()
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product name:{self.name}, description:{self.description}, price:{self.price}"


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Total_price:{self.total_price}, date_order:{self.date_ordered}"
