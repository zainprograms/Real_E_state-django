# Generated by Django 5.0 on 2024-03-13 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_propertyamenity_alter_property_amenities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='add_properties',
            field=models.ManyToManyField(blank=True, related_name='project', to='main.property'),
        ),
    ]
