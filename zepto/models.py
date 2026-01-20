from django.db import models
from django.contrib.auth.models import User

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
    

class stadium(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=150)
    capicity = models.PositiveBigIntegerField()
    home_team = models.ForeignKey(franchise,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}-{self.city}"
    
class profilepic(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10,blank=True)
    address = models.CharField(max_length=200,blank=True)
    profile_pic = models.ImageField(upload_to='profile_picc/',blank=True, null=True)
    
def __str__(self):
    return f"{self.user.username}'s profile"