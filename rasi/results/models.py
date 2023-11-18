from django.db import models
#from User.models import User

# Create your models here.

class Results(models.Model):
    
    identification = models.CharField(max_length=50)
    result = models.CharField(max_length=50 )
    medition = models.CharField(max_length=50)
    apreciation = models.CharField(max_length=50)
    
    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(result__in = ["positivo", "negativo", "inconcluso"],)
                ,name = 'resultados_permitidos'
            )
        ]

