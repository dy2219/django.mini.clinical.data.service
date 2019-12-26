from django.db import models
import datetime


class Patient(models.Model):
    first_name = models.CharField(max_length=32, default="")
    last_name = models.CharField(max_length=32, default="")
    birth = models.DateField(default=datetime.date(1900, 12, 31))
    gender = models.CharField(max_length=8, default="")
    phone_number = models.CharField(max_length=16, default="")
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    study_nurse_name = models.CharField(max_length=32, default="")
