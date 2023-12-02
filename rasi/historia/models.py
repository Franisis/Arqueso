from django.db import models

# Create your models here.


class Historia(models.Model):
    iddbauthor = models.CharField(max_length=100)
    cc = models.CharField(max_length=50)
    dateCreated = models.DateField(auto_now_add=True)
    duration = models.DecimalField(max_length=50)
    date = models.DateField( auto_now_add=False)
    time = models.CharField(max_length=50)
    motivo = models.CharField(max_length=50)
    