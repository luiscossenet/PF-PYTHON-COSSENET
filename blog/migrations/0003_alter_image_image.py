# Generated by Django 5.0.7 on 2024-08-17 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='blog/media/'),
        ),
    ]
