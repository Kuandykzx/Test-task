from django.db import models


class Banknote(models.Model):
    denominator = models.PositiveIntegerField(unique=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.denominator)

    def __unicode__(self):
        return str(self.denominator)