from log.models import Log
from django.contrib import admin
from project.models import Project
from django.db.models import Sum

# Register your models here.

@admin.register(Project)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "show_total")

    def show_total(self, obj):
        
        result = Log.objects.filter(project=obj).aggregate(Sum('duration'))
        return result["duration__sum"]

