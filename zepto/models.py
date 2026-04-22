from django.db import models
from django.contrib.auth.models import User


class Franchise(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=40)
    founded_year = models.PositiveIntegerField()

    logo_url = models.ImageField(
        upload_to="franchise_logos/",
        blank=True,
        null=True
    )

    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    country = models.CharField(max_length=80)

    class Meta:
        db_table = "franchise"

    def __str__(self):
        return f"{self.name} ({self.short_name})"




class Player(models.Model):
    ROLE_CHOICES = [
        ("Batsman", "Batsman"),
        ("Bowler", "Bowler"),
        ("All Rounder", "All Rounder"),
        ("Wicket Keeper", "Wicket Keeper"),
    ]

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    role = models.CharField(max_length=40, choices=ROLE_CHOICES)
    nationality = models.CharField(max_length=60)

    franchise = models.ForeignKey(
        Franchise,
        on_delete=models.CASCADE,
        related_name="players"
    )

    def __str__(self):
        return f"{self.name} [{self.country}]"


class Stadium(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    capacity = models.PositiveIntegerField()

    home_team = models.ForeignKey(
        Franchise,
        on_delete=models.CASCADE,
        related_name="stadiums"
    )

    def __str__(self):
        return f"{self.name} - {self.city}"

class ProfilePic(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    phone_number = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=200, blank=True)

    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"