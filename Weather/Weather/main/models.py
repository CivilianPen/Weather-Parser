from django.db import models
from .models import *
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.utils.crypto import *
import random
import string

class Cities(models.Model):
    Name = models.CharField('Название', max_length=60)
    Url = models.CharField('Ссылка', max_length=60, default='')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def get_absolute_url(self):
        return reverse("about", kwargs={"post_Name": self.Name})

