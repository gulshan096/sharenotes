from django import forms
from .models import Upload


class UploadFile(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['branch','subject','date','file']
        widgets = {
            'branch': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Branch Name'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Name'}),
            'date': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'file': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),

        }