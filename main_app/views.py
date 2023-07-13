from django.shortcuts import render
from django.http import HttpResponse
from .models import Diet, Workout, Journal, DietSerializer, WorkoutSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions



from rest_framework.views import APIView



class ListDiet(APIView):
    def get(self, request):
        diet = Diet.objects.all()
        serializer = DietSerializer(diet, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DietSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
class DietDetail(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, diet_id, user_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Diet.objects.get(id=diet_id, user = user_id)
        except Diet.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, diet_id, *args, **kwargs):
        '''
        Retrieves the diet with given diet_id
        '''
        diet_instance = self.get_object(diet_id, request.user.id)
        if not diet_instance:
            return Response(
                {"res": "Object with diet id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = DietSerializer(diet_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, diet_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        diet_instance = self.get_object(diet_id, request.user.id)
        if not diet_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'breakfast': request.data.get('breakfast'), 
            'lunch': request.data.get('lunch'), 
            'dinner': request.data.get('dinner'), 
            'snack': request.data.get('snack'), 
            'hydration': request.data.get('hydration'), 
            'date': request.data.get('date'),  
            'user': request.user.id
        }
        serializer = DietSerializer(instance = diet_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, todo_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        diet_instance = self.get_object(todo_id, request.user.id)
        if not diet_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        diet_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )