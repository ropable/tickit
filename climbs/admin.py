from django.contrib import admin
from .models import Business, Wall, Climb


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'current')


class WallAdmin(admin.ModelAdmin):
    list_display = ('name', 'current', 'business', 'climb_type', 'position')


class ClimbAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'current', 'business', 'wall', 'climb_type', 'position')


admin.site.register(Business, BusinessAdmin)
admin.site.register(Wall, WallAdmin)
admin.site.register(Climb, ClimbAdmin)