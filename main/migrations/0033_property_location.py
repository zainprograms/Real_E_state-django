# Generated by Django 5.0 on 2024-03-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_property_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=150, null=True),
        ),
    ]