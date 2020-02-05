from doctorhome import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'doctor_at_home',views.DoctoratATHomeViewSet,basename='doctorviews')
router.register('nurse',views.NureseViewSet,basename='doctornurse')
router.register('nursereportdata',views.NurseReportdataViewSet,basename='nursereportdata')
router.register('CMS',views.CMSViewSet,basename='cms')
router.register('CMS-electron',views.ElectrocardgramViewSet,basename='CMS-electron')
router.register('specility',views.SpeailityVIewSet,basename='specialityname')
router.register('hospital',views.HospitalVIewSet,basename='HOSPITAL')
router.register('fess',views.FeesViewSet,basename='fees')
urlpatterns=router.urls

