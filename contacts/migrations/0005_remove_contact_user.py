# Generated by Django 5.0.2 on 2024-02-21 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_user_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]
