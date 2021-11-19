from rest_framework import serializers
from archive.models import Session

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        #fields = ['datte', 'id_activity', 'title']
        fields = '__all__'