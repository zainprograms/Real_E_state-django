# Generated by Django 5.0 on 2024-03-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_leads_followupdate_alter_leads_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='followUpDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
