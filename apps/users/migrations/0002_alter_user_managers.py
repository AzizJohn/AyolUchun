# Generated by Django 4.1.7 on 2023-03-13 06:47

import apps.users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', apps.users.models.CustomUserManager()),
            ],
        ),
    ]
