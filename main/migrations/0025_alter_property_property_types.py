# Generated by Django 5.0 on 2024-03-15 00:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_property_property_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.propertytypes'),
        ),
    ]
