from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User

class Diet(models.Model):
    id = models.IntegerField(primary_key=True)
    breakfast = models.CharField(max_length=250)
    lunch = models.CharField(max_length=250)
    dinner = models.CharField(max_length=250)
    snack = models.CharField(max_length=250)
    hydration = models.CharField(max_length=250)
    date = models.DateField(blank=True, null=True, default="")
  


    def __str__(self):
        return self.breakfast

    class Meta:
        ordering = ['breakfast']
    

class DietSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    breakfast = serializers.CharField(max_length=250)
    lunch = serializers.CharField(max_length=250)
    dinner = serializers.CharField(max_length=250)
    snack = serializers.CharField(max_length=250)
    hydration = serializers.CharField(max_length=250)
    date = serializers.DateField(required =True)

    def create(self, validated_data):
        return Diet.objects.create(**validated_data)


class Workout(models.Model):
    id = models.IntegerField(primary_key=True)
    body_part = models.CharField(max_length=250)
    exercise = models.CharField(max_length=250)
    sets = models.CharField(max_length=250)
    reps = models.CharField(max_length=250)
    date = models.DateField(blank=True, null=True, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.body_part

    class Meta:
        ordering = ['body_part']
    
class WorkoutSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    body_part = serializers.CharField(max_length=250)
    exercise = serializers.CharField(max_length=250)
    sets = serializers.CharField(max_length=250)
    reps = serializers.CharField(max_length=250)
    date = serializers.DateField(required=True)

    def create(self, validated_data):
        return Workout.objects.create(**validated_data)

class Journal(models.Model):
    entry = models.CharField(max_length=250)
    
    date = models.DateField(blank=True, null=True, default="")

# class Journal(serializers.Serializer):
#     entry = serializers.CharField(max_length=250)
#     # diet = serializers.PrimaryKeyRelatedField(queryset=Diet.objects.all(), many =True)
#     class Meta:
#         model = Diet
#         fields = ('breakfast', 'lunch', 'dinner', 'snack', 'hydration', 'date',)
#         depth = 1
    


