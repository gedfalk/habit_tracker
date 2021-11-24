from rest_framework import serializers
from rest_framework.fields import IntegerField
from archive.models import Session
import time, datetime


# Сериализатор через ModelSerializer
class SessionListSerializer(serializers.ModelSerializer):
    in_seconds = serializers.SerializerMethodField(method_name='calculate_seconds')
    total = IntegerField()

    class Meta:
        model = Session
        fields = ['in_seconds', 'total']
    
    # перевод даты в секунды
    def calculate_seconds(self, instance):
        return int(time.mktime(instance['datte'].timetuple()))
        #return int(time.mktime(instance.datte.timetuple()))    не работает с выборками


# Сериализатор через Serializer        
class SessionSerializer(serializers.Serializer):
    #datte = serializers.DateField()
    #id_activity = serializers.CharField()  здесь только foreign key. Возможно, нужен именно ModelSerializer    
    #title = serializers.CharField()
    in_seconds = serializers.SerializerMethodField(method_name='calculate_seconds') 
    total = serializers.IntegerField()

    def calculate_seconds(self, instance):
        return int(time.mktime(instance['datte'].timetuple()))
          


'''     для отладки в python shell

from archive.models import Session
from django.db.models import Count
from tracker.api.serializers import SessionSerializer
from tracker.api.serializers import SessionListSerializer

S = Session.objects.all()
ses1 = S.values('datte').filter(id_activity__shortname_activity="IT").annotate(total=Count('id_session')).order_by()

'''