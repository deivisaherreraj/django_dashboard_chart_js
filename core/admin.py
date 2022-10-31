from django.contrib import admin

from core.models import DomesticViolence, Gender, TypeDomesticViolence, ViolentDeaths, TypeViolentDeaths

# Register your models here.

# GENERO


class GenderInline(admin.TabularInline):
    model = Gender


class GenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(Gender, GenderAdmin)


# MUERTES VIOLENTAS
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

#--------- FIN MUERTE VIOLENCIA ------------#

# VIOLENCIA INTRAFAMILIAR


class TypeDomesticViolenceInline(admin.TabularInline):
    model = TypeDomesticViolence


class TypeDomesticViolenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(TypeDomesticViolence, TypeDomesticViolenceAdmin)


class DomesticViolenceInline(admin.TabularInline):
    model = DomesticViolence


class DomesticViolenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'type', 'gender')


admin.site.register(DomesticViolence, DomesticViolenceAdmin)
