# Generated by Django 5.0 on 2024-03-13 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_project_add_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='amenities',
            field=models.ManyToManyField(to='main.amenity'),
        ),
        migrations.DeleteModel(
            name='PropertyAmenity',
        ),
    ]
