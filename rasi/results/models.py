from django.db import models

# Create your models here.

class Result(models.Model):
    result = models.CharField(max_length=50, null = True)    
    datetime = models.DateTimeField(auto_now_add=True)
    meaurement = models.CharField(max_length=50, null = True)
    apreciation = models.CharField(max_length=50, null = True)

def __str__(self):
    return '%s %s' % (self.result, self.apreciation)
