from django.contrib import admin

from .models import Session

#admin.site.unregister(Session)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id_session', 'id_activity', 'title', 'date', 'description')


