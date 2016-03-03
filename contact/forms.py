from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Your name:")
    contact_email = forms.EmailField(required=True, label="Your email:")
    contact_subject = forms.CharField(required=True, label="Your subject:")
    content = forms.CharField(required=True, widget=forms.Textarea, label="What do you want to say?")
