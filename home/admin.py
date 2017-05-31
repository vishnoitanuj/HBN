from django.contrib import admin
from .models import Innovation, Activities

class InnovationModelAdmin(admin.ModelAdmin):
    list_display = ["title", "innovator", "updatedtime","timestamp"]
    list_filter = ["updatedtime", "innovator", "title"]
    search_fields = ["title","detail"]
    class Meta:
        model = Innovation

admin.site.register(Innovation, InnovationModelAdmin)
admin.site.register(Activities)