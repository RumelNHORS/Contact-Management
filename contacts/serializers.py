from rest_framework import serializers
# from .models import Contact
from contacts import models as contact_models
from django.core.exceptions import ValidationError
import re


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = contact_models.Contact
        # fields = ['id', 'name', 'email', 'phone_number', 'address']
        fields = '__all__'

    def validate_email(self, value):
        """
        Check if the email already exists in the database.
        """
        if contact_models.Contact.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
    
    def validate_phone_number(self, value):
        """
        Validate the phone number format.
        """
        # Define a simple regex for a valid phone number format
        phone_number_regex = re.compile(r'^\+?[0-9]\d{1,14}$')

        if not phone_number_regex.match(value):
            raise serializers.ValidationError("Invalid phone number format.")

        return value
