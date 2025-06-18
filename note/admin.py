from django.contrib import admin
from .models import Notes
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','date']
    list_filter = ['title']
    search_fields = ('title',)
    list_editsble = ('title','description')
    list_per_page = 5
    
admin.site.register(Notes,NoteAdmin)