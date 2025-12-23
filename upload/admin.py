from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'uploaded_at')
    readonly_fields = ('uploaded_at',)
