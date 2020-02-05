from patients import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('patient',views.PatiensViewSet,basename='patient'),
router.register('patient-family',views.FamilyViewSet,basename='family'),
router.register('patient-report',views.ReportViewSet,basename='report')

urlpatterns=router.urls