from django.db import models

# Create your models here.
class CalculatorOperation(models.Model):
    expression = models.CharField(max_length=255)
    result = models.FloatField()

    def __str__(self):
        return f"{self.expression} = {self.result}"