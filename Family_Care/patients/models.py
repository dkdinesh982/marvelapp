from django.db import models
from doctor.models import *
# from Appointment.models import *

class Patients(models.Model):
    patients=models.OneToOneField(MyUser,on_delete=models.CASCADE,related_name='patients')
    
    dob=models.DateField()
    family_member=models.IntegerField()
    action=models.CharField(max_length=100)
    gender=(
        ('male','male'),
        ('female','female')
    )
    sex=models.CharField(choices=gender,max_length=10)

    
    def __str__(self):
        return self.action
    
class Family_Patients(models.Model):
    familtpatient=models.ForeignKey(Patients,on_delete=models.CASCADE,related_name='patient')
    name=models.CharField(max_length=100)
    relations_to_patients=models.CharField(max_length=100)
    profiles=models.ImageField(upload_to='Images',null=True)
    def __str__(self):
        return self.name

class Report(models.Model):
    report=models.ForeignKey(Patients,on_delete=models.CASCADE,related_name='reports')
    file_name=models.FileField(upload_to='Report_file',null=True)
    file_size=models.IntegerField()
    date_uploaded=models.DateField()
    action=models.CharField(max_length=10)
    def __str__(self):
        return self.action
# class Appointment(models.Model):
#     appointment=models.ForeignKey(Appointment,on_delete=models.CASCADE)