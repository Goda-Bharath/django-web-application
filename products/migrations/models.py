from django.db import models

class productsdata(models, Model):
    productname = models. CharField(max_length=100);
    productprice  = models.IntegerField()
    
def __str__(self):
    return self.productname

