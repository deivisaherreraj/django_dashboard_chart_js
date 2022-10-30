from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class TypeViolentDeaths(models.Model):
    name = models.CharField(max_length=80, help_text="Tipo de muerte")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class ViolentDeaths(models.Model):
    year = models.IntegerField(validators=[MaxValueValidator(9999)])
    type = models.ForeignKey(TypeViolentDeaths, on_delete=models.CASCADE)

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        # return '%s (%s)' % (self.id, self.book.title)
        return '{0} {1} {2}'.format(self.id, self.year, self.type.name)
