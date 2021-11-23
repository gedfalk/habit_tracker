from rest_framework import serializers
from rest_framework.fields import IntegerField
from archive.models import Session
import time, datetime

class SessionSer(serializers.Serializer):
    datte = serializers.DateField()
    id_activity = serializers.IntegerField(source='author.shortname_activity')
    title = serializers.CharField()

class SessionSerializer(serializers.ModelSerializer):
    in_seconds = serializers.SerializerMethodField(method_name='calculate_seconds')  
    class Meta:
        model = Session
        fields = ['datte', 'id_activity', 'title', 'in_seconds']
    
    # перевод даты в секунды
    def calculate_seconds(self, instance):
        return int(time.mktime(instance.datte.timetuple()))

class SessionListSerializer(serializers.ModelSerializer):
    in_seconds = serializers.SerializerMethodField(method_name='calculate_seconds')
    total = IntegerField()

    class Meta:
        model = Session
        fields = ['datte', 'total', 'in_seconds']
    
    # перевод даты в секунды
    def calculate_seconds(self, instance):
        return int(time.mktime(instance.datte.timetuple()))
        #return 1234