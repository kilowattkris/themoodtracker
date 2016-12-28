from django.contrib import admin
from tracker.models import Mood

# Register your models here.
class MoodAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fiels = ['date_added']

admin.site.register(Mood, MoodAdmin)