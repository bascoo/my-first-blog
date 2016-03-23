from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Naam'}), label = "")
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}), label = "") 
    contact_subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Onderwerp'}), label = "")
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Uw vraag of opmerking'}), label = "")
