from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer

# Import necessary modules for Django REST framework views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# View to retrieve all items using GET method
class GetItems(APIView):
    def get(self, request):
        # Fetch all items from the database using Django ORM query
        items = Item.objects.all()  # ORM query
        # Serialize the queryset to convert it into JSON data
        serializer = ItemSerializer(items, many=True)  # many - all records
        # Return the serialized data as a JSON response
        return Response(serializer.data)

# View to create a new item using POST method
class CreateItem(APIView):
    def post(self, request):
        # Create a serializer instance with the data from the request
        serializerobj = ItemSerializer(data=request.data)
        # Check if the data is valid according to the serializer
        if serializerobj.is_valid():
            # Save the valid data to the database
            serializerobj.save()
            # Return the serialized data as a JSON response with status 201 (Created)
            return Response(serializerobj.data, status=status.HTTP_201_CREATED)
        # If the data is not valid, return errors with status 400 (Bad Request)
        return Response(serializerobj.errors, status=status.HTTP_400_BAD_REQUEST)

# View to update an existing item using PUT method
class UpdateItem(APIView):
    def put(self, request, pk):
        # Retrieve the existing item from the database based on the primary key (pk)
        item = Item.objects.get(pk=pk)
        # Create a serializer instance with the existing item and updated data from the request
        serializerobj = ItemSerializer(item, data=request.data)

        # Check if the updated data is valid according to the serializer
        if serializerobj.is_valid():
            # Save the valid updated data to the database
            serializerobj.save()
            # Return the serialized updated data as a JSON response
            return Response(serializerobj.data)
        # If the updated data is not valid, return errors with status 400 (Bad Request)
        return Response(serializerobj.errors, status=status.HTTP_400_BAD_REQUEST)

# View to delete an existing item using DELETE method
class DeleteItem(APIView):
    def delete(self, request, pk):
        # Retrieve the existing item from the database based on the primary key (pk)
        item = Item.objects.get(pk=pk)
        # Delete the item from the database
        item.delete()
        # Return a JSON response indicating successful deletion with status 204 (No Content)
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

