from django import forms
from .models import Patient, MedicalProfessional, User

class PatientForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'identification', 
            'regimen', 
            'contact',
            'entity', 
            'tipoIdentificacion', 
            'correo',
            
        ]

class MedicalProfessionalForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'identification', 
            'regimen', 
            'contact',
            'entity', 
            'tipoIdentificacion', 
            'correo',
            
        ]
