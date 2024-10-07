from django.db import models

class Products(models.Model):
  title = models.CharField(max_length=200)
  price = models.FloatField()
  discount_price = models.FloatField()
  category = models.CharField(max_length=200)
  description = models.TextField()
  image = models.CharField(max_length=300)

  class Meta:
    verbose_name_plural = "Products"  # This will control the plural display name in the admin interface

  def __str__(self):
    return self.title
  

class Order(models.Model):
  items = models.CharField(max_length=1000)
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  address = models.CharField(max_length=1000)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  zipcode = models.CharField(max_length=200)


  def __str__(self):
    return self.name