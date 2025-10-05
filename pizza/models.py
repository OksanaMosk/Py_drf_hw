
from django.db import models

class PizzaModel(models.Model):
    class Meta:
        db_table= "Pizzas"

    name = models.CharField(max_length=30)
    size = models.IntegerField()
    price = models.IntegerField()
    ingredients =models.JSONField(default=list)
    time_prepared = models.IntegerField()


