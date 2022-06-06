from django.contrib import admin
from log.models import Log

# Register your models here.

class LogAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['user', 'project', 'duration','remarks', 'date', 'is_late']
    
admin.site.register(Log, LogAdmin)
