# Generated by Django 5.0 on 2024-03-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_property_amenities_property_amenities'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenity',
            name='owner',
            field=models.IntegerField(default=1),
        ),
    ]
