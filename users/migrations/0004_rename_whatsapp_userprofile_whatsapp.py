# Generated by Django 5.0.7 on 2024-08-19 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_tiktok_userprofile_whatsapp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='whatsApp',
            new_name='whatsapp',
        ),
    ]
