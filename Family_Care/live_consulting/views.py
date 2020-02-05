from django.shortcuts import render

# Create your views here.
from .models import *
from patients.models import *
from doctordemo.models import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class LiveConsultingViewSet(ViewSet):
    def create(self,request):
        doctor_id=request.data.get('doctor_id')
        doctordata=Doctor_profiles.objects.get(id=doctor_id)
        print('ddddddd',doctordata)
        patient_id=request.data.get('patient_id')
        patientdata=Patients.objects.get(id=patient_id)
        print('ppppp',patientdata)
        report_id=request.data.get('report_id')
        reportsdata=Report.objects.get(id=report_id)
        print('rrrrr',reportsdata)

        liveconsultingdata=LiveConsulting()
        liveconsultingdata.patient=patientdata
        liveconsultingdata.doctors=doctordata
        liveconsultingdata.reports=reportsdata
        liveconsultingdata.no_id=request.data.get('no_id')
        liveconsultingdata.user_name=request.data.get('user_name')
        liveconsultingdata.specialty=request.data.get('specialty')
        liveconsultingdata.date=request.data.get('date')
        liveconsultingdata.call_type=request.data.get('call_type')
        liveconsultingdata.status=request.data.get('status')
        liveconsultingdata.charge=request.data.get('charge')
        liveconsultingdata.save()
        return Response({'dataa':'data created successfully'})


    def list(self,request):
        liveconsulting=LiveConsulting.objects.all()
        liveconsulting_list=[]
        for liveconsulting in liveconsulting:
            liveconsulting_list.append({
                'id':liveconsulting.id,
                'no_id':liveconsulting.no_id,
                'user_name':liveconsulting.user_name,
                'specialty':liveconsulting.specialty,
                'call_type':liveconsulting.call_type,
                'date':liveconsulting.date,
                'doctor name':liveconsulting.doctors.doctor.name,
                'patients name':liveconsulting.patient.patients.name,
                'report name':liveconsulting.reports.file_name.url
            })

        return Response({'data':liveconsulting_list})
   

    def retrieve(self,request,pk=None):
        liveconsultingdata=LiveConsulting.objects.filter(id=pk)
        liveconsultingretrivedata=LiveConsulting.objects.all()
        doctor_data_data=[]
        for liveconsultingretrivedata in liveconsultingretrivedata:
            doctor_data_data.append(liveconsultingretrivedata.doctors.doctor.name)
        liveconsultingdata_list=[]
        l=[]
        reportdata_list=[]
        patientsdetails=[]
        doctor_details_list=[]
        for liveconsultingdata in liveconsultingdata:
            reportdata_list.append({
                'name':liveconsultingretrivedata.reports.file_name.url,
                'file_size':liveconsultingretrivedata.reports.file_size,
                'date_uploaded':liveconsultingretrivedata.reports.date_uploaded,
                'action':liveconsultingretrivedata.reports.action,
            })

            doctor_details_list.append({
                'name':liveconsultingdata.doctors.doctor.name,
                'email':liveconsultingdata.doctors.doctor.email,
                'mobile':liveconsultingdata.doctors.doctor.mobile,
                'experince':liveconsultingdata.doctors.experince,
                'blood ':liveconsultingdata.doctors.blood_Group,
                'address':liveconsultingdata.doctors.address,
                'action':liveconsultingdata.doctors.action,
                

            })
            patientsdetails.append({
                'name':liveconsultingdata.patient.patients.name,
                'email':liveconsultingdata.patient.patients.email,
                'mobile':liveconsultingdata.patient.patients.mobile,
                'gender':liveconsultingdata.patient.sex,
                'dob':liveconsultingdata.patient.dob,
            })

            liveconsultingdata_list.append({
                'id':liveconsultingdata.id,
                'id no':liveconsultingdata.no_id,
                'user name':liveconsultingdata.user_name,
                'specialty':liveconsultingdata.specialty,
                'date':liveconsultingdata.date,
                'call_type':liveconsultingdata.call_type,
                'status':liveconsultingdata.status,
                'charge':liveconsultingdata.charge,
                
            })
        livedata={
            
            'user details':patientsdetails,
            'Doctor details':doctor_details_list,
            'doctor list':doctor_data_data,
            'live consulting reports':liveconsultingdata_list,
            'report Details':reportdata_list,
        }
        
           
        return Response({'response':livedata})
