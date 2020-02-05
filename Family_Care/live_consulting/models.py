from django.db import models
from doctordemo.models import *
from patients.models import *

# Create your models here.
class LiveConsulting(models.Model):
    no_id=models.IntegerField()
    user_name=models.CharField(max_length=100)
    specialty=models.CharField(max_length=100)
    date=models.DateField()
    # date=models.DateTimeField()
    call_type=(
        ('audio call','audio call'),
        ('video call','video call')
    )
    call_type=models.CharField(choices=call_type,max_length=15)
    doctors=models.ForeignKey(Doctor_profiles,on_delete=models.CASCADE,related_name='doctorliveconsulting')
    

    patient=models.ForeignKey(Patients,on_delete=models.CASCADE,related_name='patientsliveconsulting')
    reports=models.ForeignKey(Report,on_delete=models.CASCADE,related_name='reportliveconsulting')
    
    status=models.CharField(max_length=100)
    charge=models.FloatField()
    def __str__(self):
        return self.user_name