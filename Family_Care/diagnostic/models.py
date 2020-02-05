from django.db import models


from patients.models import *
from doctordemo.models import *

# Create your models here.


class Diagnostic(models.Model):
    test=models.CharField(max_length=100)
    date=models.DateField()
    # time=models.DateTimeField()
    address=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    charge=models.FloatField()
    mobile_no=models.BigIntegerField()
    def __str__(self):
        return self.username
    
class Diagnostic_detail(models.Model):
    patientpatients=models.ForeignKey(Patients,on_delete=models.CASCADE,related_name='patientsdiagnostic')
    doctordiagnostic=models.ForeignKey(Doctor_profiles,on_delete=models.CASCADE,related_name='doctordiagnostic')
    diagnostics=models.ForeignKey(Diagnostic,on_delete=models.CASCADE,related_name='diagnostic')

    subtest=models.CharField(max_length=100)
    # charge=models.CharField(max_length=100)
    
    date=models.DateField()
    charge=models.IntegerField()
    file_name=models.CharField(max_length=100)
    files=models.FileField(upload_to='diagnosticfiles',null=True)
   

    def __str__(self):
        return self.subtest
