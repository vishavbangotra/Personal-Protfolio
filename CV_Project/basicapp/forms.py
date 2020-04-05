from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Enter your first name'}),label='')
    email = forms.EmailField(max_length=100,widget= forms.EmailInput(attrs={'placeholder':'Enter your email'}),label='')
    phonenumber = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'(xxx)xxx-xxxx'}),label='')

    class Meta:
        model = Contact
        fields = '__all__'
