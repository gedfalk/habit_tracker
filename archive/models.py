from django.db import models

from django.utils import timezone
import datetime
from tracker.models import Activity

class Session(models.Model):
    id_session = models.BigAutoField(primary_key=True)
    id_activity = models.ForeignKey(Activity, on_delete=models.PROTECT, related_name='id_activityy')        # related_name='...' навертел, но пока так
    title = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    datte = models.DateField(default=datetime.date.today)
    count_unit = models.IntegerField()                                          # выставить диапазон
    id_theme = models.IntegerField()                                            # разобраться... должен хранить уникальный id "активности"
    description = models.TextField(blank=True)

    # сортировка вывода по дате
    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title

'''
class Book(models.Model):
    pass

class Podcast(models.Model):
    pass

class It(models.Model):
    pass
'''
