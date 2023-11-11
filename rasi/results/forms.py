from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = [
            'result',
            #datetime
            'meaurement', 
            'apreciation',

        ]
        labels = {
            'result': 'Result',
            #datetime: 'Datetime',
            'meaurement': 'Measurement', 
            'apreciation': 'Apreciation',
        }