from django import forms
# from .models import Contact
from contacts import models as contact_models


# This is the Form For adding the Contact Details
class ContactForm(forms.ModelForm):
    class Meta:
        model = contact_models.Contact
        fields = ['name', 'email', 'phone_number', 'address']
