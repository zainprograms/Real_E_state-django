# Generated by Django 5.0 on 2024-03-19 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_alter_leads_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
