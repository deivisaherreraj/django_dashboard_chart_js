from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

# TABLAS COMUNES

# GENDER


class Gender(models.Model):
    name = models.CharField(max_length=80, help_text="Tipo de muerte")

    class Meta:
        verbose_name = ("Genero")
        verbose_name_plural = ("Generos")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

# VIOLENT DEATHS


class TypeViolentDeaths(models.Model):
    name = models.CharField(max_length=80, help_text="Tipo de muerte")

    class Meta:
        verbose_name = ("Tipo de muerte violenta")
        verbose_name_plural = ("Tipo de muerte violentas")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class ViolentDeaths(models.Model):
    year = models.IntegerField(validators=[MaxValueValidator(9999)])
    type = models.ForeignKey(TypeViolentDeaths, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Muerte violenta")
        verbose_name_plural = ("Muertes violentas")

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        # return '%s (%s)' % (self.id, self.book.title)
        return '{0} {1} {2}'.format(self.id, self.year, self.type.name)


# DOMESTIC VIOLENCE domestic violence
class TypeDomesticViolence(models.Model):
    name = models.CharField(max_length=80, help_text="Tipo de violencia")

    class Meta:
        verbose_name = ("Tipo de violencia domestica")
        verbose_name_plural = ("Tipos de violencia domestica")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class DomesticViolence(models.Model):
    year = models.IntegerField(validators=[MaxValueValidator(9999)])
    type = models.ForeignKey(TypeDomesticViolence, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Violencia domestica")
        verbose_name_plural = ("Violencia domestica")

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        # return '%s (%s)' % (self.id, self.book.title)
        return '{0} {1} {2} {3}'.format(self.id, self.year, self.type.name, self.gender.name)

# VIVIENDAS


class BuiltBy(models.Model):
    name = models.CharField(max_length=80, help_text="Construidas por")

    class Meta:
        verbose_name = ("Contruido por")
        verbose_name_plural = ("Contruido por")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class LivingPlace(models.Model):
    year = models.IntegerField(validators=[MaxValueValidator(9999)])
    stratum = models.IntegerField()
    builtby = models.ForeignKey(BuiltBy, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Residencia")
        verbose_name_plural = ("Residencias")

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        # return '%s (%s)' % (self.id, self.book.title)
        return '{0} {1} {2} {3}'.format(self.id, self.year, self.stratum, self.builtby.name)


# INFRAESTRUCTURA VIAL
class StateInfrastructure(models.Model):
    name = models.CharField(
        max_length=80, help_text="Estado de la infraestructura vial")

    class Meta:
        verbose_name = ("Estado de infraestructura")
        verbose_name_plural = ("Estados de infraestructuras")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class TypeInfrastructure(models.Model):
    name = models.CharField(
        max_length=80, help_text="Tipo de la infraestrutura vial")

    class Meta:
        verbose_name = ("Tipo de infraestructura")
        verbose_name_plural = ("Tipos de infraestructuras")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class InfrastructureRoad(models.Model):
    year = models.IntegerField(validators=[MaxValueValidator(9999)])
    state = models.ForeignKey(StateInfrastructure, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeInfrastructure, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Infraestructura vial")
        verbose_name_plural = ("Infraestructuras viales")

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        # return '%s (%s)' % (self.id, self.book.title)
        return '{0} {1} {2} {3}'.format(self.id, self.year, self.state.name, self.type.name)


# MOVILIDAD

class VehicleType(models.Model):
    name = models.CharField(max_length=80, help_text="Tipo de vehiculo")

    class Meta:
        verbose_name = ("Tipo de vehiculo")
        verbose_name_plural = ("Tipos de vehiculos")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Vehicle(models.Model):
    year = models.IntegerField(validators=[MaxValueValidator(9999)])
    plate = models.CharField(max_length=7, help_text="Placa del vehiculo")
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Vehiculo")
        verbose_name_plural = ("Vehiculos")

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        # return '%s (%s)' % (self.id, self.book.title)
        return '{0} {1} {2} {3}'.format(self.id, self.year, self.plate, self.type.name)
