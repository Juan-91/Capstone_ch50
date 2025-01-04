from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length= 150, widget=forms.TextInput(attrs={ ' placeholder': 'Your Name' }))
    email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={ 
        'placeholder': 'Your Email',
        'type': 'email'
        }))
    message = forms.CharField(widget=forms.Textarea(attrs={ 'placeholder': 'Your Message'}))