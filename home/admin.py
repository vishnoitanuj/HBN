from django.contrib import admin
from .models import Innovation, Activities, Announcement, NetworkMember

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

admin.site.register(Innovation, InnovationModelAdmin)
admin.site.register(Activities)
admin.site.register(Announcement, AnnouncementModelAdmin)
admin.site.register(NetworkMember)