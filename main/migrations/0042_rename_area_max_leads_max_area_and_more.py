# Generated by Django 5.0 on 2024-03-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_leads_area_max_leads_area_min'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leads',
            old_name='area_max',
            new_name='max_area',
        ),
        migrations.RenameField(
            model_name='leads',
            old_name='area_min',
            new_name='max_budget',
        ),
        migrations.AddField(
            model_name='leads',
            name='min_area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='leads',
            name='min_budget',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='leads',
            name='status',
            field=models.CharField(choices=[('Attempted', 'attempted'), ('Unattempted', 'unattempted')], default='Unattempted', max_length=50),
        ),
    ]