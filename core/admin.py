from django.contrib import admin

from core.models import ViolentDeaths, TypeViolentDeaths

# Register your models here.

# admin.site.register(ViolentDeaths)
# admin.site.register(TypeViolentDeaths)


class TypeViolentDeathsInline(admin.TabularInline):
    model = TypeViolentDeaths


class TypeViolentDeathsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(TypeViolentDeaths, TypeViolentDeathsAdmin)


class ViolentDeathsInline(admin.TabularInline):
    model = ViolentDeaths


class ViolentDeathsAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'type')


admin.site.register(ViolentDeaths, ViolentDeathsAdmin)
