from django.shortcuts import render

from archive.models import Session
from django.db.models import Count

def tracker_calendar(request):
    S = Session.objects.all()

    sessions = {}
    sessions = S.values('id_activity__name_activity').annotate(total=Count('id_session')).order_by()
   

    return render(request, 'tracker/calendar.html', {'sessions': sessions})



