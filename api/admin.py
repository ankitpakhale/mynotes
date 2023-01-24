from django.contrib import admin
from .models import Note
# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display=['body', 'updated','created']
    search_fields=['body', 'updated','created']
