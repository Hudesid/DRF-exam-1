from rest_framework import viewsets
from . import serializers, models


class VehicleAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer


class SensorAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorSerializer


class SensorValueAPIViewSet(viewsets.ModelViewSet):
    queryset = models.SensorValue.objects.all()
    serializer_class = serializers.SensorValueSerializer

class MaintenanceAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Maintenance.objects.all()
    serializer_class = serializers.MaintenanceSerializer


class ServiceCenterAPIViewSet(viewsets.ModelViewSet):
    queryset = models.ServiceCenter.objects.all()
    serializer_class = serializers.ServiceCenterSerializer
