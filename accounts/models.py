<<<<<<< HEAD
from django.db import models


from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age=models.PositiveBigIntegerField(null=True,blank=True)
=======
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
>>>>>>> bb8d60eaff9c79db86becab91c8e18145f023ed4
