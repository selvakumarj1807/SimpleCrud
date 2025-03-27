from django import forms
from app.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'mobile', 'gmail']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile'}),
            'gmail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
        }
