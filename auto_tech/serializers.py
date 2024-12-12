from django.utils import timezone
from rest_framework import serializers
from . import models


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = ('id', 'model', 'year', 'vin')

    def validate_year(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Moshinani sanasi kelajakda bo'lolmaydi.")
        return value

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sensor
        fields = ('id', 'type', 'vehicle_id', 'installed_date')

    def validate_installed_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Moshinani sensor yuklangan sanasi kelajakda bo'lolmaydi.")
        return value


class SensorValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SensorValue
        fields = ('id', 'sensor_id', 'value', 'timestamp')


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Maintenance
        fields = ('id', 'vehicle_id', 'service_type', 'scheduled_date')

    def validate_scheduled_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Rejalashtirilgan sana o‘tmishda bo‘lishi mumkin emas.")
        return value

class ServiceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceCenter
        fields = ('id', 'name', 'address', 'rating')





