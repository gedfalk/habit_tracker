from django.shortcuts import render, get_object_or_404

from .models import Session

def session_list(request):
    context = {}
    sessions = Session.objects.all()
    context['sessions'] = sessions

    context['colors'] = {'blue': ['779BED', 'A1BCFF'],
                         'green': ['xxxxxxx', 'xxxxxxx'],
                         'violet': ['xxxxxxx', 'xxxxxxx']}

    return render(request, 'archive/list.html', context)



