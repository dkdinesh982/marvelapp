from django.db import models
from doctordemo.models import *
from patients.models import *
class Doctor_at_home(models.Model):
    no_id=models.IntegerField()
    doctor_name=models.ForeignKey(Doctor_profiles,on_delete=models.CASCADE,related_name='doctorhome')
    charge=models.CharField(max_length=100)
    patients_name=models.ForeignKey(Patients,on_delete=models.CASCADE,related_name='patienthome')
    # reports=models.ForeignKey(Report,on_delete=models.CASCADE,related_name='reporthome')
    name=models.CharField(max_length=10)
    file_name=models.FileField(upload_to='doctor_at_home',null=True)
    def __str__(self):
        return self.doctor_name.doctor.name

    

class NurseData(models.Model):
    nursedoctor=models.ForeignKey(Doctor_profiles,on_delete=models.CASCADE,related_name='datadoctornurse')

    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.CharField(max_length=13)
    exprience=models.CharField(max_length=100)
    hospital=models.CharField(max_length=100)
    fees=models.FloatField()
    caretype=models.CharField(max_length=100)
    natureofcare=models.CharField(max_length=100)
    typing=models.CharField(max_length=100)
    days=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class NurseReportdata(models.Model):
    nursedata=models.ForeignKey(NurseData,on_delete=models.CASCADE,related_name='nursedata')
    name=models.CharField(max_length=100)
    files=models.FileField(max_length=100)
    def __str__(self):
        return self.name



class Diagnostcms(models.Model):
    test=models.CharField(max_length=100)
    testamount=models.FloatField()
    action=models.CharField(max_length=100)
    def __str__(self):
        return self.test
class Electrocardgram(models.Model):
    diagnost=models.ForeignKey(Diagnostcms,on_delete=models.CASCADE,related_name='electrogram')
    subtest=models.CharField(max_length=100)
    amount=models.FloatField()
    def __str__(self):
        return self.subtest
class Speciality(models.Model):
    speciality_name=models.CharField(max_length=100)
    def __str__(self):
        return self.speciality_name

class HospitalRegister(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    time=models.DateTimeField()
    documents_and_files=models.FileField(upload_to='documents_and_files',null=True,blank=True)
    def __str__(self):
        return self.name

class Fees(models.Model):
    name=models.CharField(max_length=100)
    charge=models.FloatField()
    def __str__(self):
        return self.name
    
    