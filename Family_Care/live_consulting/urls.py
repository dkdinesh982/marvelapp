from live_consulting import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('liveconsulting',views.LiveConsultingViewSet,basename='liveconsulting')
urlpatterns=router.urls
