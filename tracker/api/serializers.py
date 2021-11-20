from rest_framework import serializers
from archive.models import Session
import time, datetime

class SessionSerializer(serializers.ModelSerializer):
    in_seconds = serializers.SerializerMethodField(method_name='calculate_seconds')
    
    class Meta:
        model = Session
        fields = ['datte', 'id_activity', 'title', 'in_seconds']
    
    # перевод даты в секунды
    def calculate_seconds(self, instance):
        return int(time.mktime(instance.datte.timetuple()))