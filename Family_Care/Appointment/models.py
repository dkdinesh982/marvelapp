from django.db import models
from doctordemo.models import *
from doctor.models import *
from patients.models import *

# Create your models here.
class Appointment(models.Model):
    no_id=models.IntegerField()
    time=models.DateTimeField()
    speciality=models.CharField(max_length=100)
    resonforconsulation=models.CharField(max_length=256)
    doctor_name=models.ForeignKey(Doctor_profiles,on_delete=models.CASCADE,related_name='doctor_name')
    patients_name=models.ForeignKey(Patients,on_delete=models.CASCADE,related_name='patients_name')
    status=models.CharField(max_length=100)
    def __str__(self):
        return self.user_name
