from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import ShiftCodeFormSerializers, ShiftCodeStringSerializers, ShiftFormSerializers, ShiftStringSerializers

from .models import Shift, ShiftCode

######################## Shift Code ##############################

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def shift_code_list_and_create(request):
    
    if request.method == "GET":
        code = ShiftCode.objects.all()
        serializers = ShiftCodeStringSerializers(code, many=True)
        return Response(serializers.data)
    
    elif request.method == "POST":
        serializers = ShiftCodeFormSerializers(data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id

        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def shift_code_edit_and_delete(request, pk):
    
    if request.method == 'PUT':
        shift_code = ShiftCode.objects.get(id=pk)
        serializers = ShiftCodeFormSerializers(instance=shift_code, data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id

        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)

    elif request.method == 'DELETE':
        shift_code = ShiftCode.objects.get(id=pk)
        shift_code.delete()
    return Response(serializers.data)


######################## Shift ##############################

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def shift_list_and_create(request):
    
    if request.method == "GET":
        shift = Shift.objects.all()
        serializers = ShiftStringSerializers(shift, many=True)
        return Response(serializers.data)
    
    elif request.method == "POST":
        serializers = ShiftFormSerializers(data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id

        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def shift_edit_and_delete(request, pk):
    
    if request.method == 'PUT':
        shift = Shift.objects.get(id=pk)
        serializers = ShiftFormSerializers(instance=shift, data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id

        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)

    elif request.method == 'DELETE':
        shift_code = Shift.objects.get(id=pk)
        shift_code.delete()
    return Response(serializers.data)