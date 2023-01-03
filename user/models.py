from django.db import models
from django.contrib.auth.models import AbstractUser


class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    lng = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(AbstractUser):
    UNKNOWN = "unknown"
    AUTHOR= "author"
    ADMINISTRATOR = "administrator"
    ROLE = [(UNKNOWN, "unknown"), (AUTHOR, "author"), (ADMINISTRATOR, "administrator")]

    role = models.CharField(max_length=14, choices=ROLE, default=UNKNOWN)
    age = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
