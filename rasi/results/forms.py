from django import forms
from .models import Results

class resultsForm(forms.ModelForm):
    class Meta:
        model = Results
        fields = [
            'identification',
            'result',
            'medition',
            'apreciation',
        ]
    