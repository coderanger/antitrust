from django.contrib import admin
from antitrust.models import EveItem, EveItemPrices

class EveItemPriceInline(admin.TabularInline):
    model = EveItemPrices

class EveItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'eve_id', 'eve_group_id']
    inlines = [EveItemPriceInline]

admin.site.register(EveItem, EveItemAdmin)
