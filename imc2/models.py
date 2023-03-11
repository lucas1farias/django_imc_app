

from django.db import models


class Imc(models.Model):
    result = models.CharField('Resultado de cálculo de IMC', max_length=5)

    def __str__(self):
        return self.result

    class Meta:
        verbose_name = 'Imc'
        verbose_name_plural = 'Imcs'
