from django import forms
from .models import Historia


class HistoryForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = [
            "iddbauthor",
            "cc",
            #"dateCreated",
            "duration",
            "date",
            "time", 
            "motivo",
        ]