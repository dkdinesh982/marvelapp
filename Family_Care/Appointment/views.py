from django.shortcuts import render
from patients.models import *
from .models import *
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class AppontmentViewSet(ViewSet):
    def create(self,request):
        doctordataappointment=Doctor_profiles.objects.get(id=request.data.get('doctor_id'))
        patientsdataappoinment=Patients.objects.get(id=request.data.get('patient_id'))
        appointment=Appointment()
        appointment.doctor_name=doctordataappointment
        appointment.patients_name=patientsdataappoinment
        appointment.no_id=request.data.get('no_id')
        
        appointment.time=request.data.get('time')
        # appointment.date=request.data.get('date')
        appointment.speciality=request.data.get('speciality')
        appointment.resonforconsulation=request.data.get('resonforconsulation')
       
        appointment.status=request.data.get('status')
        appointment.save()
        return Response({'response':'created successfully'})

    def list(self,request):
        appoinmentdata=Appointment.objects.all()
        appoinmentdatalist=[]
        for appoinmentdata in appoinmentdata:
            appoinmentdatalist.append({
                'id':appoinmentdata.id,
                'User Name':appoinmentdata.patients_name.patients.name,
                'Mobile':appoinmentdata.patients_name.patients.mobile,
                'Email':appoinmentdata.patients_name.patients.email,
                'Date':appoinmentdata.time,
                'Status':appoinmentdata.status,
                'Doctor Name':appoinmentdata.doctor_name.doctor.name,
                'Fees':appoinmentdata.doctor_name.charge,

            })
        return Response({'data list':appoinmentdatalist})
    def retrieve(self,request,pk=None):
        appoinment_data=Appointment.objects.filter(id=pk)
        appoinment_data_list=[]
        user_data_list=[]
        doctorappoinmentlist=[]
        for appoinment_data in appoinment_data:
            appoinment_data_list.append({
                
            })
            user_data_list.append({
                'User Name':appoinment_data.patients_name.patients.name,
                'Email':appoinment_data.patients_name.patients.email,
                'Mobile':appoinment_data.patients_name.patients.mobile,
                'Date Of Birth':appoinment_data.patients_name.dob,
                'Gender':appoinment_data.patients_name.sex,
                

            })
            doctorappoinmentlist.append({
                'Doctor Name':appoinment_data.doctor_name.doctor.name,
                'Email':appoinment_data.doctor_name.doctor.email,
                'Mobile':appoinment_data.doctor_name.doctor.mobile,
                'Exprience':appoinment_data.doctor_name.experince,
                
                'Fees':appoinment_data.doctor_name.charge,
                
            })
            appoinment_data_list.append({
                'Speciality':appoinment_data.speciality,
                'Date':appoinment_data.time,
                'Status':appoinment_data.status,
                'Reason for consult':appoinment_data.resonforconsulation,
                'charge':appoinment_data.doctor_name.charge,
                
            })
        data=[{
            
            'User Details':user_data_list,
            'Doctor Details':doctorappoinmentlist,
            'Appointment Details':appoinment_data_list,
        }]
        return Response({'response':data})
        