from django.db import models

#descreve o que quero adicionar ao banco de dados
class User(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    weight = models.DecimalField(max_digit=4, decimal_places=2)
    height = models.DecimalField(max_digit=4, decimal_places=2)
    email = models.CharField(max_length=45)
    percentageFat = models.DecimalField(max_digit=4, decimal_places=2)
    sickness = models.CharField(max_length=45)
    intolerance = models.CharField(max_length=45)
    physicalActivity = models.BoolField()
    medicines = models.CharField(max_length=45)
    sex = models.CharField(max_length=10)


    def _str_(self):
        return self.name
