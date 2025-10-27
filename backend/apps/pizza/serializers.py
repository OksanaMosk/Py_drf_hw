from rest_framework import serializers

from .models import PizzaModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = ('id', 'name', 'price', 'size', 'ingredients', 'time_prepared', 'day', 'created_at', 'updated_at')

    def validate_price(self, price):
        if price <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return price

    def validate(self, attrs):
        price = attrs.get('price')
        size = attrs.get('size')
        if price == size:
            raise serializers.ValidationError('Price cannot be equal to size')
        return attrs