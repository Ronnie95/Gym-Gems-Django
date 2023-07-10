from django.db import models

class Diet(models.Model):
    breakfast = models.CharField(max_length=250)
    lunch = models.CharField(max_length=250)
    dinner = models.CharField(max_length=250)
    postworkout = models.CharField(max_length=250)
    snack = models.CharField(max_length=250)
    hydration = models.CharField(max_length=250)

