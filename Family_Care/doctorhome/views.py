from django.shortcuts import render
from patients.models import *
from doctordemo.models import Doctor_profiles
from .models import *
# Create your views here.
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework import viewsets

class DoctoratATHomeViewSet(viewsets.ViewSet):
    def create(self,request):
        doctor_data=Doctor_profiles.objects.get(id=request.data.get('doctor_id'))
        patients_name=Patients.objects.get(id=request.data.get('patient_id'))
        
        doctor_at_home=Doctor_at_home()
        
        doctor_at_home.no_id=request.data.get('no_id')
        
        doctor_at_home.doctor_name=doctor_data
        doctor_at_home.patients_name=patients_name
        doctor_at_home.name=request.data.get('name')
        doctor_at_home.file_name=request.data.get('file_name')
        doctor_at_home.save()
        return Response({'data':'created successfully'})
    
    def list(self,request):
        doctor_at_home=Doctor_at_home.objects.all()
        doctor_at_home_list=[]
        for doctor_at_home in doctor_at_home:
            doctor_at_home_list.append({
                'id':doctor_at_home.id,
                'no_id':doctor_at_home.no_id,
                'doctor name':doctor_at_home.doctor_name.doctor.name,
                'doctor mobile':doctor_at_home.doctor_name.doctor.mobile,
                'Patient name':doctor_at_home.patients_name.patients.name,
                'patients date of birth':doctor_at_home.patients_name.dob,
                'emergency':'yes',
                # 'date':doctor_at_home.doctor_name.date,
                'charge':doctor_at_home.doctor_name.charge,})
        return Response({'response':doctor_at_home_list})

    def retrieve(self,request,pk=None):
        doctor_at_home=Doctor_at_home.objects.filter(id=pk)
        doctor_at_home_list=[]
        patients_data_list=[]
        medical_report_list=[]
        for doctor_at_home in doctor_at_home:
            doctor_at_home_list.append({
                
                
                'doctor name':doctor_at_home.doctor_name.doctor.name,
                'doctor mobile':doctor_at_home.doctor_name.doctor.mobile,
                'email':doctor_at_home.doctor_name.doctor.email,
                'Exprience':doctor_at_home.doctor_name.experince,
                'charge':doctor_at_home.doctor_name.charge,
            })
            patients_data_list.append({
                'Patient name':doctor_at_home.patients_name.patients.name,
                'email':doctor_at_home.patients_name.patients.email,
                'mobile':doctor_at_home.patients_name.patients.mobile,
                'Gender':doctor_at_home.patients_name.sex,
                'age':doctor_at_home.patients_name.dob,
                

            })
        medical_report_list.append({
            'name':doctor_at_home.name,
            'file_name':doctor_at_home.file_name.url
        })

        data=[{
            'Doctor Details':doctor_at_home_list,
            'Patient Details':patients_data_list,
            'Medical reports':medical_report_list
        }]
        return Response({'response':data})

class NureseViewSet(viewsets.ViewSet):
    def create(self,request):
        doctordata=Doctor_profiles.objects.get(id=request.data.get('doctor_id'))
        nurse=NurseData()
        nurse.nursedoctor=doctordata
        nurse.name=request.data.get('name')
        nurse.email=request.data.get('email')
        nurse.mobile=request.data.get('mobile')
        nurse.exprience=request.data.get('exprience')
        nurse.hospital=request.data.get('hospital')
        nurse.fees=request.data.get('fees')
        nurse.caretype=request.data.get('caretype')
        nurse.natureofcare=request.data.get('natureofcare')
        nurse.typing=request.data.get('typing')
        nurse.days=request.data.get('days')
        nurse.save()
        return Response({'response':'created successfully'})
    def list(self,request):
        nursedata=NurseData.objects.all()
        nursedata_list=[]
        for nursedata in nursedata:
            nursedata_list.append({
                'id':nursedata.id,
                'User Name':nursedata.name,
                'Nurse Name':nursedata.nursedoctor.doctor.name,
                'Care Type':nursedata.caretype,
                'Typing':nursedata.typing,
                'Mobile No':nursedata.mobile,
                'Days':nursedata.days,
                'Charge':nursedata.nursedoctor.charge,
            })
        return Response({'response':nursedata_list})
    def retrieve(self,request,pk=None):
        doctor_data=Doctor_profiles.objects.all()
        doctor_data_list=[]
        for doctor_data in doctor_data:
            doctor_data_list.append({
                'Nurse Doctor Name':doctor_data.doctor.name,
            })
        nurserepotrdata=NurseReportdata.objects.filter(id=pk)
        nursedatareport=NurseData.objects.filter(id=pk)
        nuresereportslist=[]
        for nursedata in nursedatareport:
            for nurse_data in nursedata.nursedata.all():
                nuresereportslist.append({
                    'name':nurse_data.name,
                    'files':nurse_data.files.url,

                })

        nurserepotrdata_list=[]
        userdata_list=[]
        
        for nurserepotrdata in nurserepotrdata:
           
            userdata_list.append({
                'User Name':nurserepotrdata.nursedata.name,
                'email':nurserepotrdata.nursedata.email,
                'mobile':nurserepotrdata.nursedata.mobile,
                'email':nurserepotrdata.nursedata.email,
                'dob':'1993-10-11',
                'email':nurserepotrdata.nursedata.email,
                'address':'noida secor 62 h-192'


            })
            nurserepotrdata_list.append({
                'Nurse Name':nurserepotrdata.nursedata.nursedoctor.doctor.name,
                'Email':nurserepotrdata.nursedata.nursedoctor.doctor.email,
                'Mobile':nurserepotrdata.nursedata.nursedoctor.doctor.mobile,
                'Exprience':nurserepotrdata.nursedata.nursedoctor.experince,
                'Fees':nurserepotrdata.nursedata.nursedoctor.charge,
                # 'Hospita Name':nurserepotrdata.nursedata.nursedoctor.hospital,
            })
            
        data=[{
                'User Details':userdata_list,
                'Nurse  Doctor all List ':doctor_data_list,
                'Nurse Doctor Details':nurserepotrdata_list,
                'Reports':nuresereportslist,
                
            }]
        return Response({'response':data})
class NurseReportdataViewSet(viewsets.ViewSet):
   
    def create(self,request):
        nursedata=NurseData.objects.get(id=request.data.get('nurse_id'))
        nursedatareports=NurseReportdata()
        nursedatareports.nursedata=nursedata
        nursedatareports.name=request.data.get('name')
        nursedatareports.files=request.data.get('files')
        nursedatareports.save()
        return Response({'response':'created successfully'})
     
class CMSViewSet(viewsets.ViewSet):
    def create(self,request):
        diagnosticcms=Diagnostcms()
        diagnosticcms.test=request.data.get('test')
        diagnosticcms.testamount=request.data.get('testamount')
        diagnosticcms.action=request.data.get('action')
        diagnosticcms.save()
        return Response({'response':'created successfull'})
    def list(self,request):
        diangostdata=Diagnostcms.objects.all()
        diangostdata_list=[]
        for diangostdata in diangostdata:
            diangostdata_list.append({
                'id':diangostdata.id,
                'test':diangostdata.test,
                'test amount':diangostdata.testamount
            })
        return Response({'data list':diangostdata_list})
class ElectrocardgramViewSet(viewsets.ViewSet):
    def create(self,request):
        diagnosticcms=Diagnostcms.objects.get(id=request.data.get('diagnosticsm_id'))
        electrogram=Electrocardgram()
        electrogram.diagnost=diagnosticcms
        electrogram.subtest=request.data.get('subtest')
        electrogram.amount=request.data.get('amount')
        electrogram.save()
        return Response({'response':'created successfully'})
    def retrieve(self,request,pk=None):
        electrogramdata=Diagnostcms.objects.filter(id=pk)
        electrogramdatalist=[]
        total=0
        for electrogramdata in electrogramdata:
            for electrogram_data in electrogramdata.electrogram.all():
                total+=electrogram_data.amount
                electrogramdatalist.append({
                    'Test':electrogram_data.diagnost.test,
                    'Sub Test':electrogram_data.subtest,
                    'Amount':electrogram_data.amount,
                })
            
        data=[{
            'Electrogram(EKG) ':electrogramdatalist,
            'Total':total,
        }]
        return Response({'response':data})
    def destroy(self,request,pk=None):
        diagnosticsm=Diagnostcms.objects.filter(id=pk).delete()
        return Response({'response':'deleted data successfully'})


class SpeailityVIewSet(viewsets.ViewSet):
    def create(self,request):
        speciality=Speciality()
        speciality.speciality_name=request.data.get('speciality_name')
        speciality.save()
        return Response({'response':'created data successfully'})
    def list(self,request,pk=None):
        speailcitydata=Speciality.objects.all()
        speailcitydata_list=[]
        for speailcitydata in speailcitydata:
            speailcitydata_list.append({
                'speciality':speailcitydata.speciality_name
            })
        return Response({'data':speailcitydata_list})
    def retrieve(self,request,pk=None):
        # name=Speciality.GET.get('name')
        data=Speciality.objects.filter(id=pk)
        data_list=[]
        for data in data:
            data_list.append({
                'name':data.speciality_name
            })
        return Response({'data':data_list})            

    def destroy(self,request,pk=None):
        data=Speciality.objects.get(id=pk).delete()
        return Response({'data':'data is deleted'})

class HospitalVIewSet(viewsets.ViewSet):
    def create(self,request):
        hospitalregister=HospitalRegister()
        hospitalregister.name=request.data.get('name')
        hospitalregister.location=request.data.get('location')
        hospitalregister.time=request.data.get('time')
        hospitalregister.documents_and_files=request.data.get('documents_and_files')
        hospitalregister.save()
        return Response({'response':'created data successfully'})

    def list(self,request,pk=None):
        hospitaldata=HospitalRegister.objects.all()
        hospitaldata_list=[]
        for hospitaldata in hospitaldata:
            hospitaldata_list.append({
                'name':hospitaldata.name,
                'date':hospitaldata.time,
                'location':hospitaldata.location,
                'documents and files':hospitaldata.documents_and_files.url,

            })
        return Response({'data':hospitaldata_list})
    def retrieve(self,request,pk=None):
        hospitalregister=HospitalRegister.objects.filter(id=pk)
        hospitalregister_list=[]
       
        for hospitalregister in hospitalregister:
            # data=hospitalregister.time.split('T')
            # datalist.append(data)
            hospitalregister_list.append({
                'id':hospitalregister.id,
                'name':hospitalregister.name,
                'date':hospitalregister.time,
                'location':hospitalregister.location,
                'documents and files':hospitalregister.documents_and_files.url,


            })
        return Response({'data':hospitalregister_list})
    def destroy(self,request,pk=None):
        data=HospitalRegister.objects.filter(id=pk).delete()
        return Response({'data':data})



class FeesViewSet(viewsets.ViewSet):
    def list(self,request):
        fees=Fees.objects.all()
        fees_list=[]
        for fees in fees:
            fees_list.append({
                'id':fees.id,
                'name':fees.name,
                'charge':fees.charge
            })
        return Response({'data':fees_list})
    def retrieve(self,request,pk=None):
        fees=Fees.objects.filter(id=pk)
        fees_list=[]
        for fees in fees:
            fees_list.append({
                'id':fees.id,
                'name':fees.name,
                'chrge':fees.charge
            })
        return Response({'data':fees_list})