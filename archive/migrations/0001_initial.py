# Generated by Django 3.2.7 on 2021-10-31 15:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id_session', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('count_unit', models.IntegerField()),
                ('id_theme', models.IntegerField()),
                ('description', models.TextField()),
                ('id_activity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archive.activity')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
