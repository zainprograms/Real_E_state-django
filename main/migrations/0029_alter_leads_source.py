# Generated by Django 5.0 on 2024-03-15 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_leads_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='Source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.source'),
        ),
    ]
