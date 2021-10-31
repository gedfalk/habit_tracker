from django.contrib import admin

from .models import Activity

#admin.site.register(Activity)
#admin.site.unregister(Activity)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id_activity', 'shortname_activity', 'name_activity', 'unit')
    