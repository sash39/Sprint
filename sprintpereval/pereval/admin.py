from django.contrib import admin

from .models import PerevalAdded, Coords, Images, Level, Users


class PerevalAdmin(admin.ModelAdmin):
    list_display = ('id', 'beauty_title', 'title', 'other_titles', 'add_time', 'user', 'coords', 'level', 'connect', 'status')

class CoordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'height')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'pereval', 'title', 'date_added')


class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'winter', 'summer', 'autumn', 'spring')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'fam', 'name', 'otc', 'phone_regex', 'phone')


admin.site.register(PerevalAdded, PerevalAdmin)
admin.site.register(Coords, CoordsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Users, UsersAdmin)
