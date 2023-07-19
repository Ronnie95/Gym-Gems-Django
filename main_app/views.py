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

    def post(self, request, *args, **kwargs):
        serializer = DietSerializer(data=request.data)
        
       
        if serializer.is_valid():
            instance = serializer.save()
            response_data = serializer.data
            response_data["id"] = instance.id
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Create your views here.
class DietDetail(APIView):
    # add permission to check if user is authenticated
   

    def get_object(self, diet_id,):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Diet.objects.get(id=diet_id,)
        except Diet.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, diet_id, *args, **kwargs):
        '''
        Retrieves the diet with given diet_id
        '''
        diet_instance = self.get_object(diet_id,)
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
        diet_instance = self.get_object(diet_id,)
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
            
        }
        serializer = DietSerializer(instance = diet_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, diet_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        diet_instance = self.get_object(diet_id,)
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
    

class ListWorkout(APIView):
    def get(self, request,*args, **kwargs):
        workout = Workout.objects.all()
        serializer = WorkoutSerializers(workout, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        data = {
            'body_part': request.data.get('body_part'),
            'exercise': request.data.get('exercise'),
            'sets': request.data.get('sets'),
            'reps': request.data.get('reps'),
            'date': request.data.get('date'),
        }
        serializer = WorkoutSerializers(data=request.data)
        
        if serializer.is_valid():
            instance = serializer.save()
            response_data = serializer.data
            response_data["id"] = instance.id
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Create your views here.
class WorkoutDetail(APIView):
    # add permission to check if user is authenticated
    

    def get_object(self, workout_id, ):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Workout.objects.get(id=workout_id, )
        except Workout.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, workout_id, *args, **kwargs):
        '''
        Retrieves the diet with given diet_id
        '''
        workout_instance = self.get_object(workout_id,)
        if not workout_instance:
            return Response(
                {"res": "Object with breakfast id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = WorkoutSerializers(workout_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, workout_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        workout_instance = self.get_object(workout_id,)
        if not workout_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'body_part': request.data.get('body_part'), 
            'exercise': request.data.get('exercise'), 
            'sets': request.data.get('sets'), 
            'reps': request.data.get('reps'), 
            'date': request.data.get('date'),  
            'user': request.user.id
        }
        serializer = WorkoutSerializers(instance = workout_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, workout_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        workout_instance = self.get_object(workout_id,)
        if not workout_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        workout_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )