# Generated by Django 5.0 on 2024-03-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_project_add_properties_project_add_properties'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.IntegerField(default=1),
        ),
    ]