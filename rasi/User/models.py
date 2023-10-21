from django.db import models


class User(models.Model):
    
    name = models.CharField(max_length=50)
    identification = models.CharField(unique=True, max_length=15)
    regimen = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    entity = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=50, null=True)
    tipoIdentificacion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50, unique=True)

    
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    emergencyContact = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.user.name)
class MedicalProfessional(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.user.name)

