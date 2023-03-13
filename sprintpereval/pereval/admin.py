from django.contrib import admin

from .models import PerevalAdded


class PerevalAddedAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_added', 'status')

admin.site.register(PerevalAdded, PerevalAddedAdmin)
