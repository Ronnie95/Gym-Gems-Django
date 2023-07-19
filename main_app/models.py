from django.db import models
from rest_framework import serializers


class Journal(models.Model):
    date = models.DateField(blank=True, null=True, default="")

    class Meta:
        ordering = ['date']

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

    def update(self, instance, validated_data):
        instance.breakfast = validated_data.get('breakfast', instance.breakfast)
        instance.lunch = validated_data.get('lunch', instance.lunch)
        instance.dinner = validated_data.get('dinner', instance.dinner)
        instance.snack = validated_data.get('snack', instance.snack)
        instance.hydration = validated_data.get('hydration', instance.hydration)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

class Workout(models.Model):
    id = models.IntegerField(primary_key=True)
    body_part = models.CharField(max_length=250)
    exercise = models.CharField(max_length=250)
    sets = models.CharField(max_length=250)
    reps = models.CharField(max_length=250)
    date = models.DateField(blank=True, null=True, default="")
    #journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name="journals")
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
    
    def update(self, instance, validated_data):
        instance.body_part = validated_data.get('body_part', instance.body_part)
        instance.exercise = validated_data.get('exercise', instance.exercise)
        instance.sets = validated_data.get('sets', instance.sets)
        instance.reps = validated_data.get('reps', instance.reps)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance



# class Journal(serializers.Serializer):
#     entry = serializers.CharField(max_length=250)
#     # diet = serializers.PrimaryKeyRelatedField(queryset=Diet.objects.all(), many =True)
#     class Meta:
#         model = Diet
#         fields = ('breakfast', 'lunch', 'dinner', 'snack', 'hydration', 'date',)
#         depth = 1
    


