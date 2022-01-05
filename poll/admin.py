from django.contrib import admin
from django.db.models.aggregates import Count
from . models import Poll

class PollAdmin(admin.ModelAdmin):
    list_display=('Question','Name_1','Name_2','image_1','image_2','count_1','count_2','total','poll_id')

admin.site.register(Poll,PollAdmin)

# Register your models here.
