# Generated by Django 3.2.7 on 2021-11-17 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0003_alter_session_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
