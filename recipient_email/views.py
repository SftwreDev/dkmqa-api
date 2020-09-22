from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .serializers import RecipientEmailFormSerializers , RecipientEmailStringSerializers
from .models import Recipient_Email


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def email_list_and_create(request):
    
    if request.method == "GET":
        email = Recipient_Email.objects.all()
        serializers = RecipientEmailStringSerializers(email, many=True)
        return Response(serializers.data)
    
    elif request.method == "POST":
        serializers = RecipientEmailFormSerializers(data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id

        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def email_edit_and_delete(request, pk):
    
    if request.method == 'PUT':
        email = Recipient_Email.objects.get(id=pk)
        serializers = RecipientEmailFormSerializers(instance=email, data=request.data)
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id

        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)

    elif request.method == 'DELETE':
        email = Recipient_Email.objects.get(id=pk)
        email.delete()
    return Response(serializers.data)