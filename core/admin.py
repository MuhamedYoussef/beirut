from django.contrib import admin
from .models import AidRecord

@admin.register(AidRecord)
class AidRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')