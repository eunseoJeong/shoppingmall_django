from django.db import models
# Create your models here.
class Product(models.Model):
    pdname = models.CharField(max_length=50)
    pdprice = models.CharField(max_length=30, null = True)
    pdbody = models.TextField()
    pdimage = models.ImageField(upload_to="product/", blank=True, null=True)

