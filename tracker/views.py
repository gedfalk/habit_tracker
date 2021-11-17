from django.shortcuts import render

from archive.models import Session

def tracker_calendar(request):
    sessions = Session.objects.all()
    sessions = sessions.filter(id_activity=3)       #настроить фильтр через foreign key

    return render(request, 'tracker/calendar.html', {'sessions': sessions})

