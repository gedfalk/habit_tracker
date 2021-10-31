from django.shortcuts import render, get_object_or_404

from .models import Session

def session_list(request):
    sessions = Session.objects.all()
    return render(request, 'archive/list.html', {'sessions': sessions})



