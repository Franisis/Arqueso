from django.db import models
from datetime import date
from User.models import User
# Create your models here.


class RegisterUser(models.Model):
    dateRegister = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

