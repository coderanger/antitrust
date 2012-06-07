from django.contrib import admin
from antitrust.models import EveItem

class EveItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'eve_id', 'eve_group_id']

admin.site.register(EveItem, EveItemAdmin)
