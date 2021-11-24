from rest_framework import generics
from archive.models import Session
from .serializers import SessionSerializer

from django.db.models import Count

class SessionListView(generics.ListAPIView):
    queryset = Session.objects.values('datte').filter(id_activity__shortname_activity="IT").annotate(total=Count('id_session')).order_by()
    serializer_class = SessionSerializer