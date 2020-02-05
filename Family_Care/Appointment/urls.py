from Appointment import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('appointment',views.AppontmentViewSet,basename='appointment')
urlpatterns=router.urls