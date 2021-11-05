from django.db import models
from django.db.models.fields import NullBooleanField

class Activity(models.Model):
    id_activity = models.AutoField(primary_key=True)
    name_activity = models.CharField(max_length=30)
    shortname_activity = models.CharField(max_length=3, default='OOO')
    unit = models.SmallIntegerField()
    color = models.CharField(max_length=20, default='white')
    # id_table

    def __str__(self):
        return self.name_activity

    