from django.contrib import admin
from .models import Business, Wall, Rope, Climb, Rating


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'current')
    prepopulated_fields = {'slug': ('name',)}


class WallAdmin(admin.ModelAdmin):
    list_display = ('name', 'current', 'business', 'climb_type', 'position')


class RopeAdmin(admin.ModelAdmin):
    list_display = ('name', 'current', 'wall')


class ClimbAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'current', 'business', 'wall', 'climb_type', 'position',
        'grade')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'climb', 'like')


admin.site.register(Business, BusinessAdmin)
admin.site.register(Wall, WallAdmin)
admin.site.register(Rope, RopeAdmin)
admin.site.register(Climb, ClimbAdmin)
admin.site.register(Rating, RatingAdmin)
