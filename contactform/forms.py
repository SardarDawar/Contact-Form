from django import forms

class contact(forms.Form):
    Name = forms.CharField(max_length=100)
    Email = forms.EmailField(max_length=100)
    Contact=forms.CharField()
    Message = forms.CharField(
     widget=forms.TextInput(attrs={'placeholder': 'Message'}))