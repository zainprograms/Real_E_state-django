# Generated by Django 5.0 on 2024-03-15 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_property_property_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_types',
            field=models.CharField(choices=[('residential', 'Residential'), ('commercial', 'Commercial'), ('other', 'Other')], max_length=50),
        ),
    ]