
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pizza.models import PizzaModel
from pizza.serializers import PizzaSerializer


class PizzaCreateView(APIView):
    def get(self,*args,**kwargs):
        pizzas = PizzaModel.objects.all()
        serializer = PizzaSerializer(instance=pizzas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,*args,**kwargs):
        data=self.request.data
        serializer = PizzaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class PizzaRetrieveUpdateDestroyView(APIView):
    def get(self,*args,**kwargs):
        pk=self.kwargs.get('pk')
        try:
            pizza = PizzaModel.objects.get(pk=pk)
        except PizzaModel.DoesNotExist:
            return Response(f'Pizza {pk} does not exist', status=status.HTTP_404_NOT_FOUND)
        serializer = PizzaSerializer(pizza)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,*args,**kwargs):
        pk=self.kwargs.get('pk')
        try:
            pizza = PizzaModel.objects.get(pk=pk)
        except PizzaModel.DoesNotExist:
            return Response(f'Pizza {pk} does not exist', status=status.HTTP_404_NOT_FOUND)
        data=self.request.data
        serializer = PizzaSerializer(instance=pizza, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,*args,**kwargs):
        pk=kwargs.get('pk')
        try:
            pizza=PizzaModel.objects.get(pk=pk)
            pizza.delete()
            return Response(f'Pizza {pk} deleted', status=status.HTTP_204_NO_CONTENT)
        except PizzaModel.DoesNotExist:
            return Response(f'Pizza {pk} does not exist', status=status.HTTP_404_NOT_FOUND)





