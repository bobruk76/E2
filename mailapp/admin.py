from django.contrib import admin

# Register your models here.
from mailapp.models import Task


@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    pass