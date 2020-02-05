from doctor import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('reg',views.registerViewSet,basename='register')
router.register('login',views.LoginViewSet,basename='login')

urlpatterns=router.urls