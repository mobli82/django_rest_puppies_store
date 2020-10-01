from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PuppyModel
from .serializers import PuppySerializer

@api_view(['GET', 'DELETE','PUT'])
def get_delete_update_puppy(request, pk):
    try:
        puppy = PuppyModel.objects.get(pk=pk)
    
    except PuppyModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # get details of single puppy
    if request.method == 'GET':
        serializer = PuppySerializer(puppy)
        return Response(serializer.data)

    # delete single puppy
    elif request.method == 'DELETE':
        puppy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    # update details of single puppy
    elif request.method == 'PUT':
        serializer = PuppySerializer(puppy, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_puppies(request):
    # get all puppies
    if request.method == 'GET':
        puppies = PuppyModel.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data)
    
    #inser new puppy
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'age': int(request.data.get('age')),
            'breed': request.data.get('breed'),
            'color': request.data.get('color'),
        }
        serializer = PuppySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    