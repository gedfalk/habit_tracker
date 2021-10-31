from django.db import models

class Activity(models.Model):
    id_activity = models.AutoField(primary_key=True)
    name_activity = models.CharField(max_length=30)
    shortname_activity = models.CharField(max_length=3, default='OOO')
    unit = models.SmallIntegerField()
    # id_table

    def __str__(self):
        return self.name_activity

    