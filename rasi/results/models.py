from django.db import models
#from User.models import User

# Create your models here.

class Results(models.Model):
    OPCIONES_RESULTADO = (
        ("positivo", "positivo"),
        ("negativo", "negativo"),
        ("inconcluso", "inconcluso"),
    )
    identification = models.CharField(max_length=50)
    resultado = models.CharField(max_length=50, choices=OPCIONES_RESULTADO)
    medition = models.CharField(max_length=50)
    apreciation = models.CharField(max_length=50)
    
    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(resultado__in = ["positivo", "negativo", "inconcluso"],)
                ,name = 'resultados_permitidos'
            )
        ]

