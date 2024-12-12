from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'vehicles', views.VehicleAPIViewSet)
router.register(r'vehicles/(?P<vehicle_pk>\d+)/sensors', views.SensorAPIViewSet)
router.register(r'sensors/(?P<sensor_pk>\d+)/readings', views.SensorValueAPIViewSet)
router.register(r'maintenance/schedule', views.MaintenanceAPIViewSet)
router.register(r'service/centers', views.ServiceCenterAPIViewSet)


urlpatterns = router.urls