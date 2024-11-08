# Generated by Django 5.0 on 2024-03-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_client_owner_alter_client_client_pin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(max_length=150)),
                ('agent_contact', models.CharField(max_length=150)),
                ('agent_mail', models.EmailField(max_length=254)),
                ('agent_DOB', models.DateField()),
                ('agent_PAN', models.IntegerField()),
                ('agent_deals_in', models.CharField(max_length=100)),
                ('agent_address', models.CharField(max_length=250)),
                ('agent_city', models.CharField(max_length=100)),
                ('agent_state', models.CharField(max_length=80)),
                ('agent_pin', models.IntegerField()),
            ],
        ),
    ]