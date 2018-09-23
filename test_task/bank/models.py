from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Banknote(models.Model):
    denominator = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(1)])
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1), ])

    def __str__(self):
        return str(self.denominator)

    def __unicode__(self):
        return str(self.denominator)

    def full_clean(self, exclude=None, validate_unique=True):
        if self.denominator < 1 or self.quantity < 1:
            raise ValidationError('Only numbers equal to 1 or greater are accepted.')
