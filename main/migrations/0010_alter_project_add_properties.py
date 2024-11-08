# Generated by Django 5.0 on 2024-03-10 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_add_projects_project_add_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='add_properties',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='main.property'),
        ),
    ]
