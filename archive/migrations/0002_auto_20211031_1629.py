# Generated by Django 3.2.7 on 2021-10-31 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_activity_shortname_activity'),
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='id_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='id_activityy', to='tracker.activity'),
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
    ]
