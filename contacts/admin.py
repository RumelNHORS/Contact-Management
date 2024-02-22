from django.contrib import admin
from .models import Contact
# from contacts import models as contact_models

# Register the Contact Model to the Admin
# admin.site.register(contact_models.Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address')
    search_fields = ('name', 'email', 'phone_number', 'address')
