from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = [
            'result',
            #datetime
            'measurement', 
            'apreciation',

        ]
        labels = {
            'result': 'Result',
            #datetime: 'Datetime',
            'measurement': 'Measurement', 
            'apreciation': 'Apreciation',
        }