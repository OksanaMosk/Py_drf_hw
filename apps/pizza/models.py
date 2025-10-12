from django.db import models

from apps.pizza_shops.models import PizzaShopModel

from core.models import BaseModel


class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizza'
    name = models.CharField(max_length=30)
    price = models.FloatField()
    size = models.IntegerField()
    ingredients =models.JSONField(default=list)
    time_prepared = models.IntegerField()
    pizza_shop=models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')
