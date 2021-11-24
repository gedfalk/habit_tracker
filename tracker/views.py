from django.shortcuts import render

from archive.models import Session
from django.db.models import Count

def tracker_calendar(request):
    S = Session.objects.all()

    #sessions = {}
    #sessions['IT'] = S.values('datte').filter(id_activity__shortname_activity="IT").annotate(total=Count('id_session')).order_by()

    sessions = S.values('datte').filter(id_activity__shortname_activity="IT").annotate(total=Count('id_session')).order_by()
    

    return render(request, 'tracker/calendar.html', {'sessions': sessions})



