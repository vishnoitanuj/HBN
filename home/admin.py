from django.contrib import admin
from .models import Innovation, Activities, Announcement

class InnovationModelAdmin(admin.ModelAdmin):
    list_display = ["title", "innovator", "updatedtime","timestamp"]
    list_filter = ["updatedtime", "innovator", "title"]
    search_fields = ["title","detail"]
    class Meta:
        model = Innovation

class AnnouncementModelAdmin(admin.ModelAdmin):
    list_display = ["title","date","head"]
    list_filter = ["date", "type"]
    search_fields = ["title","url"]
    list_editable = ["head"]
    class Meta:
        model = Announcement

class ActivitiesModelAdmin(admin.ModelAdmin):
    list_display = ["act_title", "act_timestamp"]
    list_filter = ["act_title"]
    search_fields = ["act_title", "act_detail"]

    class Meta:
        model = Activities


admin.site.register(Innovation, InnovationModelAdmin)
admin.site.register(Activities, ActivitiesModelAdmin)
admin.site.register(Announcement, AnnouncementModelAdmin)