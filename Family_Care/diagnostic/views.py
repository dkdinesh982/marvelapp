from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
# Create your views here.

class DiagnosticViewSet(viewsets.ViewSet):
    def create(self,request):
        diagnostic=Diagnostic()
        diagnostic.test=request.data.get('test')
        diagnostic.date=request.data.get('date')
        diagnostic.address=request.data.get('address')
        diagnostic.username=request.data.get('username')
        diagnostic.charge=request.data.get('charge')
        diagnostic.mobile_no=request.data.get('mobile_no')
        diagnostic.save()
        return Response({'data':'created  successfully'})
    def list(self,request):
        diagnosticdata=Diagnostic.objects.all()
        diagnosticalllist=[]
        for diagnosticdata in diagnosticdata:
            diagnosticalllist.append({
                'id':diagnosticdata.id,
                'test':diagnosticdata.test,
                'username':diagnosticdata.username,
                'address':diagnosticdata.address,
                'mobile_no':diagnosticdata.mobile_no,
                'charge':diagnosticdata.charge,
            })
        return Response({'response':diagnosticalllist})
    #     diagnostic_data=Diagnostic.objects.all()
    #     diagnostic_data_list=[]
    #     for diagnostic_data in diagnostic_data:
    #         diagnostic_data_list.append({
    #             'id':diagnostic_data.id,
    #             'Test':diagnostic_data.test,
    #             'Date':diagnostic_data.date,
    #             'Address':diagnostic_data.address,
    #             'Charge':diagnostic_data.charge,
    #             'Mobile no':diagnostic_data.mobile_no,
    #         })
    #     return Response({'data list':diagnostic_data_list})
    # def retrieve(self,request,pk=None):
    #     patientdata=Patients.objects.filter(id=pk)
    #     patientdata_list=[]
    #     for patientdata in patientdata:
    #         for patientdata in patientdata.patientsdiagnostic.all():
    #             patientdata_list.append({
    #                 'id':patientdata.patientpatients.id,
    #                 'name':patientdata.patientpatients.pname,
    #                 'mobile number':patientdata.patientpatients.pmobile,
    #                 'date of birth':patientdata.patientpatients.dob,
    #                 'gender':patientdata.patientpatients.sex,
    #             })
    #     doctordata=Doctor_profiles.objects.filter(id=pk)
        
    #     doctordata_list=[]
    #     for doctordata in doctordata:
    #         for doctordata in doctordata.doctordiagnostic.all():
                
    #             doctordata_list.append({
    #                 'id':doctordata.doctordiagnostic.doctor.id,
    #                 'Name':doctordata.doctordiagnostic.doctor.name,
    #                 'Mobile':doctordata.doctordiagnostic.doctor.mobile,
    #                 'Gender':doctordata.doctordiagnostic.sex,
    #                 'Blood Group':doctordata.doctordiagnostic.blood_Group,
    #                 'Address':doctordata.doctordiagnostic.address,

    #             })
    #     # # patient_data=Patients.objects.filter(id=pk)
    #     # patients_data_list=[]
    #     # for patientdata in patient_data:
    #     #     for patientdata1 in patientdata.patientsdiagnostic.get(id=pk):
                
    #     #         patients_data_list.append({
    #     #             'id':patientdata1.patientpatients.id,
    #     #         })
                
            
            
            
            
    #     doctordata=Doctor_profiles.objects.all()
    #     doctor=[]
    #     for doctordata in doctordata:
    #         for doctordata in doctordata.doctordiagnostic.all():
    #             doctor.append({
    #                 'name':doctordata.doctordiagnostic.doctor.name,
    #             })

    #     diagnostic_data=Diagnostic.objects.filter(id=pk)
        
    #     diagnostic_list=[]
        
    #     diagnosticdatalist=[]
    #     total=0
    #     llist=[]
    #     report_list=[]
    #     report_data=DiangnosticReport.objects.filter(id=pk)
    #     for reportdata in report_data:
    #         for report_data in reportdata.diagnosticreport.all():
    #             report_list.append({
    #                 'id':report_data.reports.id,
    #                 'Name':report_data.reports.name,
    #                 'file size':report_data.reports.file_size,
    #                 'Files ':report_data.reports.files.url,
    #             })
    #     for diagnostic_data in diagnostic_data:
    #         for diadata in diagnostic_data.diagnostic.all():
    #             diagnosticdatalist.append(diadata.charge)
    #         for i in diagnosticdatalist:
    #             total+=int(i)
    #         llist.append({
    #                 'Patient Details':patientdata_list,
    #                 'Doctor Details':doctordata_list,
    #                 'diagnostic details':diagnostic_list,
    #                 'Total':total,
    #                 'Report':report_list,
    #                 'doctor list':doctor,
    #          })
    #         for diagnosticdata in diagnostic_data.diagnostic.all():
    #                 diagnostic_list.append({
    #                 'Test':diagnosticdata.test.test,
    #                 'Sub Test':diagnosticdata.subtest,
    #                 'Date':diagnosticdata.test.date,
    #                 'charge':diagnosticdata.charge,
    #                 })
        
    #     return Response({'Diagnostic Details':llist})


# class DiangnosticReportDataViewSet(viewsets.ViewSet):
#     def create(self,request):
#         diagnosticdatareport=Diagnostic.objects.get(id=request.data.get('diagnostic_id'))
#         diagnosticreportdata=DiangnosticReportData() 
#         diagnosticreportdata.diagnosticreport=diagnosticdatareport
#         diagnosticreportdata.name=request.data.get('name')
#         diagnosticreportdata.file_size=request.data.get('file_size')
#         diagnosticreportdata.files=request.data.get('files')
#         diagnosticreportdata.save()
#         return Response({'response':'report created successfully'})

#     def list(self,request):
#         data='enter the diagnostic id in ruls'
#         return Response({'response':data})
#     def retrieve(self,request,pk=None):

#         diagnosticreportdata=Diagnostic.objects.filter(id=pk)
#         # Diangnostic_ReportData_list=[]
#         diagnostic_reports=[]
#         for diagnosticreportdata in diagnosticreportdata:
#             for diagnosticreport_data in diagnosticreportdata.diagnosticreport.all():
#                 diagnostic_reports.append({
#                     'Diagnostic Details test':diagnosticreport_data.diagnosticreport.test,
#                     'Diagnostic Detailsusername':diagnosticreport_data.diagnosticreport.username,
#                     'Report name':diagnosticreport_data.name,
#                     'file_size':diagnosticreport_data.file_size,
#                     'files':diagnosticreport_data.files.url,
                    

#                 })
#         return Response({'response':diagnostic_reports})
class Diagnostic_detailViewSet(viewsets.ViewSet):
    def list(self,request):
        data="enter the diagnostic id in urls:"
        return Response({'response':data})
    def create(self,request):
        patients_data=Patients.objects.get(id=request.data.get('patients_id'))
        doctor_data=Doctor_profiles.objects.get(id=request.data.get('Doctor_profiles_id'))
        diagnosticdatadetails=Diagnostic.objects.get(id=request.data.get('diagnostic_id'))
        diagnostic_detail=Diagnostic_detail()
        diagnostic_detail.patientpatients=patients_data
        diagnostic_detail.doctordiagnostic=doctor_data
        diagnostic_detail.diagnostics=diagnosticdatadetails
        diagnostic_detail.subtest=request.data.get('subtest')
        diagnostic_detail.date=request.data.get('date')
        diagnostic_detail.file_name=request.data.get('file_name')
        diagnostic_detail.files=request.data.get('files')
        diagnostic_detail.charge=request.data.get('charge')
        diagnostic_detail.save()
        return Response({'response':'data created successully'})

    def retrieve(self,request,pk=None):
        
        diagnosticdatareport=Diagnostic_detail.objects.filter(id=pk)
        diagnostic_datareport=[]
        patientdatalist=[]
        doctotdatalist=[]
       
        doctoralldata=Doctor_profiles.objects.all()
        doctorall_datalist=[]
        for doctoralldata in doctoralldata:
            doctorall_datalist.append({'doctor name':doctoralldata.doctor.name})
        
        for diagnosticdatareport in diagnosticdatareport:

            patientdatalist.append({
                'patient name':diagnosticdatareport.patientpatients.patients.name,
                'email':diagnosticdatareport.patientpatients.patients.email,
                'mobile':diagnosticdatareport.patientpatients.patients.mobile,
                'Date Of Birth':diagnosticdatareport.patientpatients.dob,
                'Gender':diagnosticdatareport.patientpatients.sex,
               
            })
            doctotdatalist.append({
                'doctor name':diagnosticdatareport.doctordiagnostic.doctor.name,
                'email':diagnosticdatareport.doctordiagnostic.doctor.email,
                'mobile':diagnosticdatareport.doctordiagnostic.doctor.mobile,
                'Exprience':diagnosticdatareport.doctordiagnostic.experince,
                'Hospital Name':diagnosticdatareport.doctordiagnostic.address,
                'charge':diagnosticdatareport.diagnostics.charge,
       
                
            })
            diagnostic_datareport.append({
                'test':diagnosticdatareport.diagnostics.test,
                'sub test':diagnosticdatareport.subtest,
                'date':diagnosticdatareport.diagnostics.date,
                'charge':diagnosticdatareport.charge,
            })
        diagnostic_reportdata=Diagnostic.objects.filter(id=pk)
        diagnostic_reportdata_list=[]
        reportdata_list=[]
        sum=[]
        total=0
        for diagnostic_reportdata in diagnostic_reportdata:
            for diagnostic_report_data in diagnostic_reportdata.diagnostic.all():
                total+=(diagnostic_report_data.charge)
        
                diagnostic_reportdata_list.append({
                    'test':diagnostic_report_data.diagnostics.test,
                    'sub test':diagnostic_report_data.subtest,
                    'date':diagnostic_report_data.date,
                    'charge':diagnostic_report_data.charge,
                })
            
                reportdata_list.append({
                    'file name':diagnostic_report_data.file_name,
                    'files':diagnostic_report_data.files.url,
                })
            
        
        

        

        data=[{
            'diagnostic Reports':diagnostic_datareport,
            'Patients Details':patientdatalist,
            'Doctor Details':doctotdatalist,
            'Doctor List':doctorall_datalist,
            'Diagnostic Details':diagnostic_reportdata_list,
            'Total':total,
            'Report Details':reportdata_list,
            
            }]

        return Response({'response':data})


