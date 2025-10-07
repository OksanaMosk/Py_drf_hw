from django.db import models
class PizzaModel(models.Model):
    class Meta:
        db_table = 'pizza'
    name = models.CharField(max_length=30)
    price = models.FloatField()
    size = models.IntegerField()
    ingredients =models.JSONField(default=list)
    time_prepared = models.IntegerField()