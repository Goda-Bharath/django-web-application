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

class players(models.Model):
    Role_choices = [
    ("Batsman","Batsman"),
    ("Bowler","Bowler"),
    ("All_Rounder","All_Rounder"),
    ("Wicket_Keeper","Wicket_keeper"),        
]
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField()
    role = models.CharField(max_length=40, choices=Role_choices)
    nationality = models.CharField(max_length=60)
    franchise = models.ForeignKey(franchise,on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.name},[{self.country}]"