from django.contrib import admin
from .models import ClickCounter


class ClickCounterAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'counter', 'type']


admin.site.register(ClickCounter, ClickCounterAdmin)
