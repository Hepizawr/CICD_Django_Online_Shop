from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=5,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Your Full Name'}
        )
    )
    email = forms.EmailField(

        widget=forms.EmailInput(
            attrs={'placeholder': 'Enter Your email'}
        )
    )
    subject = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter subject'}
        )
    )
    message = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter Your message'}
        )
    )