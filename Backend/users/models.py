from django.db import models

#descreve o que quero adicionar ao banco de dados
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.DecimalField(max_digit=9, decimal_places=2)
    height = models.DecimalField(max_digit=9, decimal_places=2)

    def _str_(self):
        return self.name
