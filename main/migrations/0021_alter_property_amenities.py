# Generated by Django 5.0 on 2024-03-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_property_amenities_delete_propertyamenity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='amenities',
            field=models.ManyToManyField(blank=True, to='main.amenity'),
        ),
    ]
