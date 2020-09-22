from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import PersonFormSerializer , PersonStringSerializer
from .models import Person


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def person_list_or_create(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonStringSerializer(person, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PersonFormSerializer(data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def person_update_or_delete(request, pk):
    if request.method == 'PUT':
        person = Person.objects.get(id=pk)
        serializer = PersonFormSerializer(instance=person, data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE' :
        person = Person.objects.get(id=pk)
        person.delete()
        return Response("Item succesfully deleted")
