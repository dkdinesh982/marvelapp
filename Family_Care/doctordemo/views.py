from django.shortcuts import render
from doctor.models import *
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
from .models import *

class DoctorProfileVIewSet(viewsets.ViewSet):
    def create(self,request):
        # email=request.user.email
        myuser = MyUser.objects.get(email=request.user.email)
        print('email pppppp',myuser)
        doctor_profiles=Doctor_profiles()
        doctor_profiles.doctor=myuser
        doctor_profiles.blood_Group=request.data.get('blood_Group')
        doctor_profiles.experince=request.data.get('experince')
        doctor_profiles.sex=request.data.get('sex')
        doctor_profiles.address=request.data.get('address')
        doctor_profiles.charge=request.data.get('charge')
        # doctor_profiles.action=request.data.get('action')
        doctor_profiles.save()
        return Response({'data':'successfully'})
        
    def list(self,request):
        doctor_data=Doctor_profiles.objects.all()
        doctor_list=[]
        for doctor_data in doctor_data:
            doctor_list.append({
                'id':doctor_data.id,
                'doctor name':doctor_data.doctor.name,
                'email':doctor_data.doctor.email,
                'mobile no':doctor_data.doctor.mobile,
                'address':doctor_data.address,
                # 'action':doctor_data.action,
                
                
            })
        return Response({'data':doctor_list})
    def retrieve(self, request, pk=None):
        
        doctor_data1=Doctor_profiles.objects.filter(id=pk)
   
        data_retrieve=[] 
        edu_list=[]

        for doctor in doctor_data1:
           
            for edu in doctor.educations.all():
                edu_list.append({
                             
                  
                    'doctor_degree':edu.doctor_degree,
                    'university_college':edu.university_college,
                    'passing_year':edu.passing_year
                    })
                print("#$##$#$#",edu)

            
            data_retrieve.append({
                'id':doctor.id,
                'doctor name':doctor.doctor.name,
                'doctor email':doctor.doctor.email,
                'date of birth':'sb+',
                'mobile no':doctor.doctor.mobile,
                
                'education ':edu_list,
                

            })

            
                


        return Response({'retrieve data':data_retrieve})
class EducationViewSet(viewsets.ViewSet):
    def create(self,request):
        doctor_education=Doctor_profiles.objects.get(doctor=request.user)
        print("profile",doctor_education)
        education=Education()
        education.doctor_profiles=doctor_education
        education.doctor_degree=request.data.get('doctor_degree')
        education.university_college=request.data.get('university_college')
        education.passing_year=request.data.get('passing_year')
        education.save()

        return Response({'response':'created successfulyy','message':True})
    def list(self,request):
        
        education_data=Education.objects.all()
        education_list=[]
        for education_data in education_data:
            education_list.append({
                'id':education_data.id,
                'doctor_degree':education_data.doctor_degree,
                'university_college':education_data.university_college,
                'passing_year':education_data.passing_year,
                
             })
        return Response({'educations':education_list})
    def retrieve(self,request,pk=None):
        doctor_data=Doctor_profiles.objects.filter(id=pk)
        doctor_data_list=[]
        doctoreducation_list=[]
        for doctor_data in doctor_data:
            doctor_data_list.append({
                # 'id':doctor_data.doctor.id,
                'doctor name':doctor_data.doctor.name,
                'doctor email':doctor_data.doctor.email,
                'mobile number':doctor_data.doctor.mobile,
                'blood group':doctor_data.blood_Group,
                'address':doctor_data.address,
                'education retrieve':doctoreducation_list,
            })
            
        for doctoreducation in doctor_data.educations.all():
            doctoreducation_list.append({
                # 'id':doctoreducation.id,
                'doctor_degree':doctoreducation.doctor_degree,
                'university_college':doctoreducation.university_college,
                'passing_year':doctoreducation.passing_year
            })

        return Response({'education retrieve':doctor_data_list})
class DocumentsViewSet(viewsets.ViewSet):
    def create(self,request):
        doctor_documents=Doctor_profiles.objects.get(doctor=request.user)
        documents=Documents()
        documents.doctor_documents=doctor_documents
        documents.document_name=request.data.get('document_name')
        documents.date_uploaded=request.data.get('date_uploaded')
        documents.file_size=request.data.get('file_size')
        documents.action=request.data.get('action')
        documents.save()
        return Response({'response':'data'})
    def list(self,request):
        documents_data=Documents.objects.all()
        documents_data_list=[]
        for documents_data in documents_data:
            documents_data_list.append({
                'id':documents_data.id,
                'files name':documents_data.document_name.url,
                'date_uploaded':documents_data.date_uploaded,
                
                'file_size':documents_data.file_size,
                'action':documents_data.action
            })
        return Response({'d0cuments list':documents_data_list})
    
    def retrieve(self, request, pk=None):
        documents_data_retrieve=Doctor_profiles.objects.filter(id=pk)
        # # documents_data_retrieve_list=[]
        # # for documents_data_retrieve in documents_data_retrieve:
        # #     documents_data_retrieve_list.append({
        # data=[{ 
        # 'date_uploaded':documents_data_retrieve.date_uploaded,
        # # 'pp':documents_data.document_name.files,
        # 'file_size':documents_data_retrieve.file_size,
        # 'action':documents_data_retrieve.action
        #  }]
        documents_data_retrieve_list=[]
        doctor_list=[]
        for documents_data_retrieve in documents_data_retrieve:
            for documents in documents_data_retrieve.doctor_documents.all():
                documents_data_retrieve_list.append({
                    # 'documents':documents.id,
                    'file name':documents.document_name.url,
                    'date uploaded':documents.date_uploaded,
                    'file_size':documents.file_size,
                    'action':documents.action,})
            doctor_list.append({
                # 'id':documents_data_retrieve.id,
                'doctor name':documents.doctor_documents.doctor.name,
                'mobile number':documents.doctor_documents.doctor.mobile,
                'email':documents.doctor_documents.doctor.email,
                'blood group':documents.doctor_documents.blood_Group,
                'documents':documents_data_retrieve_list

            })
                
        return Response({'data retrive':doctor_list})




# class DiagnosticViewSets(viewsets.ViewSet):
#     def list(self,request):
#         diagnostic_data=Diagnostic.objects.all()
#         diagnostic_data_list=[]
#         for diagnostic_data in diagnostic_data:
#             diagnostic_data_list.append({
#                 'id':diagnostic_data.id,
#                 'Test':diagnostic_data.test,
#                 'Date':diagnostic_data.date,
#                 'Address':diagnostic_data.address,
#                 'Charge':diagnostic_data.charge,
#                 'Mobile no':diagnostic_data.mobile_no,
#             })
#         return Response({'data list':diagnostic_data_list})
#     def retrieve(self,request,pk=None):
        
        
#         diagnostic_data=Diagnostic.objects.filter(id=pk)
        
#         diagnostic_list=[]
        
#         diagnosticdatalist=[]
#         total=0
#         llist=[]
#         for diagnostic_data in diagnostic_data:
#             for diadata in diagnostic_data.diagnostic.all():
#                 diagnosticdatalist.append(diadata.charge)
#             for i in diagnosticdatalist:
#                 total+=int(i)
#             llist.append({
#                     'diagnostic details':diagnostic_list,
#                     'Total':total,
#              })
#             for diagnosticdata in diagnostic_data.diagnostic.all():
#                     diagnostic_list.append({
#                     'Test':diagnosticdata.test.test,
#                     'Sub Test':diagnosticdata.subtest,
#                     'Date':diagnosticdata.test.date,
#                     'charge':diagnosticdata.charge,
#                     })
#             return Response({'Diagnostic Details':llist})



class PharmacyViewSet(viewsets.ViewSet):
    def list(self,request):
        parmacydata=Pharmacy.objects.all()
        parmacydata_list=[]
        for parmacydata in parmacydata:
            parmacydata_list.append({
                'id':parmacydata.id,
                'Medicine Name':parmacydata.medicine_name,
                'username':parmacydata.username,
                'email':parmacydata.email,
                'address':parmacydata.address,
                'charge':parmacydata.charge,
                

            })
        return Response({'data':parmacydata_list})
    def create(self,request):
        pharmacy=Pharmacy()
        pharmacy.medicine_name=request.data.get('medicine_name')
        pharmacy.username=request.data.get('username')
        pharmacy.email=request.data.get('email')
        pharmacy.address=request.data.get('address')
        pharmacy.charge=request.data.get('charge')
        pharmacy.action=request.data.get('action')
        pharmacy.save()
        return Response({'response':'created successfully data'})
    
    def retrieve(self,request,pk=None):
        filterdata=Pharmacy.objects.filter(id=pk)
        filterdata_list=[]
        for filterdata in filterdata:
            filterdata_list.append({

                'id':filterdata.id,
                'Medicine Name':filterdata.medicine_name,
                'username':filterdata.username,
                'email':filterdata.email,
                'address':filterdata.address,
                'charge':filterdata.charge,
            })
        return Response({'data':filterdata_list})


class Pharmacy_DetailsViewSet(viewsets.ViewSet):
    def list(self,request):
        data='enter the data in urls:'
        return Response({'data':data})
    def create(self,request):
        patient_data=Patients.objects.get(id=request.data.get('patient_id'))
        pharmacy_data=Pharmacy.objects.get(id=request.data.get('pharmacy_id'))
        pharmacy_details=Pharmacy_Details()
        pharmacy_details.patientsdata=patient_data
        pharmacy_details.pharmacydata=pharmacy_data
        pharmacy_details.type=request.data.get('type')
        pharmacy_details.quantity=request.data.get('quantity')
        pharmacy_details.file_name=request.data.get('file_name')
        pharmacy_details.files=request.data.get('files')
        pharmacy_details.save()
        return Response({'response':'created created successfully'})
    def retrieve(self,request,pk=None):
        data='enter the patiernts id: in urls'
        parmacypatientdata=Patients.objects.all()
        parmacypatientdatalist=[]
        for parmacypatientdata in parmacypatientdata:
            parmacypatientdatalist.append({
                
                'name':parmacypatientdata.patients.name,
            })
        pharmacydetaildata=Pharmacy_Details.objects.filter(id=pk)
        pharmacy_detaildata_list=[]
        medicine_details_list=[]
        reportdatalist=[]
        for pharmacydetaildata in pharmacydetaildata:
            pharmacy_detaildata_list.append({
                'id':pharmacydetaildata.id,
                'user name':pharmacydetaildata.patientsdata.patients.name,
                'Mobile No.':pharmacydetaildata.patientsdata.patients.mobile,
                'Email':pharmacydetaildata.patientsdata.patients.email,
                'Date Of Birth':pharmacydetaildata.patientsdata.dob,
                'Gender':pharmacydetaildata.patientsdata.sex,
                

            })
            medicine_details_list.append({
                'Medicine name':pharmacydetaildata.pharmacydata.medicine_name,
                'Type':pharmacydetaildata.type,
                'Quantity':pharmacydetaildata.quantity,
            })
            reportdatalist.append({
                'name':pharmacydetaildata.file_name,
                'files':pharmacydetaildata.files.url
            })
        data=[{
            'All User':parmacypatientdatalist,
            'USer Details':pharmacy_detaildata_list,
            'Medicine Details':medicine_details_list,
            'Prescription Reports':reportdatalist
        }]
        return Response({'response':data})
       


