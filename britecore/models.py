from django.db import models

# Create your models here.

field_type = (('text', 'text'), ('number', 'number'), ('date', 'date'))

class Risk(models.Model):
    title = models.CharField(max_length=300)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Datatypes(models.Model):
    risk_rel = models.ForeignKey(
        Risk, related_name='datatypes', on_delete=True)
    field_name = models.CharField(max_length=300)
    field_value = models.CharField(max_length=200, blank=True, null=True)
    field_type = models.CharField(max_length=300, choices=field_type)

    def __str__(self):
        return f'{self.field_name}: {self.field_type}'
