from django.shortcuts import render
from doctor.models import *
# Create your views here.
from .models import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
class PatiensViewSet(ViewSet):
    def create(self,request):
        print('rrrrrrrrrr',request.user)
        patientsdata=MyUser.objects.get(email=request.user.email)
        print('cccccccccc',patientsdata)
        
        patient=Patients()
        patient.patients=patientsdata
        patient.dob=request.data.get('dob')
        patient.family_member=request.data.get('family_member')
        patient.sex=request.data.get('sex')
        patient.action=request.data.get('action')
        patient.save()
        return Response({'response':'created succefull ','message':True})
        
        
        
    def list(self,request):

        patients_data=Patients.objects.all()
        patients_data_list=[]
        for patients_data in patients_data:
            patients_data_list.append({
                'id':patients_data.id,
                'id no':patients_data.patients.id_no,
                'patient name':patients_data.patients.name,
                'patient email':patients_data.patients.email,
                'mobile number':patients_data.patients.mobile,
                # 'email':patients.patients.email,
                # 'mobile number':patients_data.patients.mobile,
                'Date of Birth':patients_data.dob,
                'Gender':patients_data.sex,
                'Family Member':patients_data.family_member,
                'Action':patients_data.action
            })
        
        return Response({'Patient List':patients_data_list})
    def retrieve(self,request,pk=None):
        patients_data=Patients.objects.filter(id=pk)
        patients_retrieve_list=[]
        for patients_data in patients_data:
            patients_retrieve_list.append({
                'id':patients_data.id,
                
                'id no':patients_data.patients.id_no,
                'patient name':patients_data.patients.name,
                'patient email':patients_data.patients.email,
                'mobile number':patients_data.patients.mobile,
                # 'email':patients.patients.email,
                # 'mobile number':patients_data.patients.mobile,
                'Date of Birth':patients_data.dob,
                'Gender':patients_data.sex,
                'Family Member':patients_data.family_member,
                'Action':patients_data.action
            })
        return Response({'response':patients_retrieve_list})
       
#-----------------------------------------------------------------------------------------------
        
class FamilyViewSet(ViewSet):
    def create(self,request):
        print('ppppppp',request.user)
        familypatients=Patients.objects.get(patients=request.user)
        print('ccccccc',familypatients)
        family_patientsdata=Family_Patients()

        family_patientsdata.familtpatient=familypatients
        family_patientsdata.name=request.data.get('name')
        family_patientsdata.relations_to_patients=request.data.get('relations_to_patients')
        family_patientsdata.profiles=request.data.get('profiles')
        family_patientsdata.save()
        return Response({'response':'creatded succefully'})
    # def list(self,request):
    #     data=[]
    #     return Response({'data':"enter the urs in patients id no"})

    def list(self,request):
        data='enter the patient id in urls'

        return Response({'data':data})
       
    def retrieve(self,request,pk=None):
        pdata=Patients.objects.filter(id=pk)
        p=[]
        family_list=[]
        for patients in pdata:
            for patient in patients.patient.all():
                family_list.append({
                    
                    'family name':patient.name,
                    'relations_to_patients':patient.relations_to_patients,
                    'profiles':patient.profiles.url
                })
           

        return Response({'retrieve':family_list})
class ReportViewSet(ViewSet):
    def create(self,request):
        print('rrrrrrrr',request.user)
        patientdata=Patients.objects.get(patients=request.user)
        print('pppppppp',patientdata)
        reportdata=Report()
        reportdata.report=patientdata
        reportdata.file_name=request.data.get('file_name')
        reportdata.file_size=request.data.get('file_size')
        reportdata.date_uploaded=request.data.get('date_uploaded')
        reportdata.action=request.data.get('action')
        reportdata.save()
        return Response({'reponse':'creatded successfull'})
    def list(self,request):
        data='enter the id of patients in urls'
        return Response({'data':data})
        
    def retrieve(self,request,pk=None):
        report_data=Patients.objects.filter(id=pk)
        reportdata_list=[]
        for report_data in report_data:
            for reportdataretrireve in report_data.reports.all():
                reportdata_list.append({
                    'id':reportdataretrireve.id,
                    'file name':reportdataretrireve.report.dob,
                    'file_name':reportdataretrireve.file_name.url,
                    'file_size':reportdataretrireve.file_size,
                    'date_uploaded':reportdataretrireve.date_uploaded,
                    'action':reportdataretrireve.action
                    
                })
        return Response({'data':reportdata_list})
        
       

# class AppointmentmentsViewSets(viewsets.ViewSet):
#     def create(self,request):
