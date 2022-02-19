from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from rest_framework.response import Response

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


class Webhooks(viewsets.ViewSet):

    def list(self, request):
        ''' Listing the Plant from Stored Procedure '''
        mode = self.request.query_params.get('hub.mode')
        verify_token = self.request.query_params.get('hub.verify_token')
        challenge = self.request.query_params.get('hub.challenge')


        data = {
            'hub.challenge': challenge
        }

        if mode == "subscribe" and verify_token == "bW9uZXR0ZXNjYWtlc2hvcG1vbmV0dGVzY2FrZXNob3Btb25ldHRlc2Nha2VzaG9w":
            return Response(data, status=status.HTTP_200_OK)
        return Response("HEHEHE")