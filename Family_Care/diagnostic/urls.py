from diagnostic import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('diagnostic',views.DiagnosticViewSet,basename='diagnostic')
# router.register('diagnostic-report',views.DiangnosticReportDataViewSet,basename='diagnostic-report')
router.register('diagnostic-details',views.Diagnostic_detailViewSet,basename='diagnostic-details')
urlpatterns=router.urls