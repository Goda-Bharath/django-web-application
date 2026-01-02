from django.db import models

# Create your models here.

class franchise(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=40)
    founded_year = models.IntegerField()
    logo_url = models.ImageField(upload_to="franchise_logos/", blank=True,null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    

    class Meta:
       db_table = "franchise"
       
    def __str__(self):
        return f"{self.name} (({self.short_name}))"
