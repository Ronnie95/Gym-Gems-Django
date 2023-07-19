# todo/todo_api/urls.py : API urls.py

from django.urls import path, include
from .views import (
    ListDiet,
    DietDetail,
    ListWorkout,
    WorkoutDetail
)




urlpatterns = [
    path('api/', ListDiet.as_view()),
    path('api/<int:diet_id>/', DietDetail.as_view()),
    path('api/workout/', ListWorkout.as_view()),
    path('api/workout/<int:workout_id>/', WorkoutDetail.as_view()),
]