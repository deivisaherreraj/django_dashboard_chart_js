from django.contrib import admin

from core.models import BuiltBy, DomesticViolence, Gender, InfrastructureRoad, LivingPlace, StateInfrastructure, TypeDomesticViolence, TypeInfrastructure, Vehicle, VehicleType, ViolentDeaths, TypeViolentDeaths

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

# --------- FIN MUERTE VIOLENCIA ------------#

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

# --------- FIN VIOLENCIA INTRAFAMILIAR ------------#

# VIVIENDA


class BuiltByInline(admin.TabularInline):
    model = BuiltBy


class BuiltByAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(BuiltBy, BuiltByAdmin)


class LivingPlaceInline(admin.TabularInline):
    model = LivingPlace


class LivingPlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'stratum', 'builtby')


admin.site.register(LivingPlace, LivingPlaceAdmin)

# --------- FIN VIVIENDA ------------#


# INFRAESTRUCTURA VIAL


class StateInfrastructureInline(admin.TabularInline):
    model = StateInfrastructure


class StateInfrastructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(StateInfrastructure, StateInfrastructureAdmin)


class TypeInfrastructureInline(admin.TabularInline):
    model = TypeInfrastructure


class TypeInfrastructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(TypeInfrastructure, TypeInfrastructureAdmin)


class InfrastructureRoadInline(admin.TabularInline):
    model = InfrastructureRoad


class InfrastructureRoadAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'state', 'type')


admin.site.register(InfrastructureRoad, InfrastructureRoadAdmin)

# --------- INFRAESTRUCTURA VIAL ------------#


# MOVILIDAD


class VehicleTypeInline(admin.TabularInline):
    model = VehicleType


class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(VehicleType, VehicleTypeAdmin)


class VehicleInline(admin.TabularInline):
    model = Vehicle


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'plate', 'type')


admin.site.register(Vehicle, VehicleAdmin)

# --------- MOVILIDAD ------------#
