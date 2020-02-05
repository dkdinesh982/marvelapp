from django.db import models

# Create your models here.
from doctor.models import *
from patients.models import *
# from Appointment.models import *

class Doctor_profiles(models.Model):
   
    doctor=models.OneToOneField(MyUser,on_delete=models.CASCADE,related_name="doctor_profile")
    # sex=models.CharField(choices=GENDER,max_length=1)
    blood=(
        
        ('A+','A+'),
        ('A-','A-'),
       
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-'),

    )
    experince = models.CharField(max_length=256,null=True,blank=True)
    gender=(
        ('male','male'),
        ('female','female')
    )
    sex=models.CharField(choices=gender,max_length=10)
    blood_Group = models.CharField(choices=blood,max_length=3)
    action = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    charge=models.IntegerField()
    def __str__(self):
        return self.sex

    
class Education(models.Model):
    doctor_profiles=models.ForeignKey(Doctor_profiles,on_delete=models.CASCADE,related_name='educations')

    doctor_degree=models.CharField(max_length=100)
    university_college=models.CharField(max_length=255)
    passing_year=models.CharField(max_length=4)

class Documents(models.Model):
    doctor_documents=models.ForeignKey(Doctor_profiles,on_delete=models.CASCADE,related_name='doctor_documents')
    document_name=models.FileField(upload_to='FIlres',null=True)
    date_uploaded=models.DateField()
    file_size=models.IntegerField()
    action=models.CharField(max_length=50)
    def __str__(self):
        return self.action

# class AppoinmetDoctor(models.Model):
#     id_no=models.IntegerField()
#     appoinemtnetdata=models.ForeignKey(Appointment,on_delete=models.CASCADE,related_name='appoinem')



class Pharmacy(models.Model):
    medicine_name=models.CharField(max_length=100)
    username=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.TextField()
    charge=models.IntegerField()
    action=models.FileField(upload_to='pharmacy_fields',null=True)
    def __str__(self):
        return self.medicine_name
        
class Pharmacy_Details(models.Model):
    patientsdata=models.ForeignKey(Patients,on_delete=models.CASCADE,related_name='patientsdata')
    pharmacydata=models.ForeignKey(Pharmacy,on_delete=models.CASCADE,related_name='pharmacydata')
    type=models.CharField(max_length=100)
    quantity=models.CharField(max_length=10)
    file_name=models.CharField(max_length=100)
    files=models.FileField(upload_to='pharmacy_details',null=True)
    def __str__(self):
        return self.type
