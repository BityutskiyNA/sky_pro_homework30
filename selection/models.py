from django.db import models

# Create your models here.
from ads.models import Ad
from user.models import User


class Selection(models.Model):
    items = models.ManyToManyField(Ad)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'
