from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Address, Plant
from .serializers import AdddressFormSerializer, AdddressStringSerializer, PlantFormSerializer, PlantStringSerializer


############# Address API ###############

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def address_list_or_create(request):
    if request.method == 'GET':
        address = Address.objects.all()
        serializer = AdddressStringSerializer(address, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdddressFormSerializer(data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def address_update_or_delete(request, pk):
    if request.method == 'PUT':
        address = Address.objects.get(id=pk)
        serializer = AdddressFormSerializer(instance=address, data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE' :
        address = Address.objects.get(id=pk)
        address.delete()
        return Response("Item succesfully deleted")



############# Plant API ###############

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def plant_list_or_create(request):
    if request.method == 'GET':
        plant = Plant.objects.all()
        serializer = PlantStringSerializer(plant, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlantFormSerializer(data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def plant_update_or_delete(request, pk):
    if request.method == 'PUT':
        plant = Plant.objects.get(id=pk)
        serializer = PlantFormSerializer(instance=address, data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE' :
        plant = Plant.objects.get(id=pk)
        plant.delete()
        return Response("Item succesfully deleted")