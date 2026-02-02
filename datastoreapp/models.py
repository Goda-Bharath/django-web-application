from django.db import models

class productItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12,decimal_places=4)
    discount = models.IntegerField()
    discrption = models.TextField()
    stockavb = models.IntegerField()
    image = models.ImageField(upload_to='/products_img',blank=True, null=True)

    def __str__(self):
      return self.name    
