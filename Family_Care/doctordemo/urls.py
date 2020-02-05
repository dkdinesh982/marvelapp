from doctordemo import views
# from django.urls import path,include
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('doctor',views.DoctorProfileVIewSet,basename='doctorprofiles')
router.register('education',views.EducationViewSet,basename='educations')
router.register('doctuments',views.DocumentsViewSet,basename='doctuments')
router.register('Appointments',views.DocumentsViewSet,basename='Appointments')
router.register('pharmacy',views.PharmacyViewSet,basename='pharmacy')
router.register('pharmacy-details',views.Pharmacy_DetailsViewSet,basename='pharmacy-details')

urlpatterns=router.urls