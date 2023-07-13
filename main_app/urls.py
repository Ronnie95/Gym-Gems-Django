# todo/todo_api/urls.py : API urls.py

from django.urls import path, include
from .views import (
    ListDiet,
    DietDetail
)




urlpatterns = [
    path('api', ListDiet.as_view()),
    path('api/<int:diet_id>/', DietDetail.as_view()),
]