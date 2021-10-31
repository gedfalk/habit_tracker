from django.shortcuts import render

from archive.models import Session

def tracker_calendar(request):
    sessions = Session.objects.all()
    return render(request, 'tracker/calendar.html', {'sessions': sessions})

