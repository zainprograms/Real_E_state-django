# Generated by Django 5.0 on 2024-03-18 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_alter_leads_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
