from django.db import models


class Vehicle(models.Model):
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    vin = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Model: {self.model} Year: {self.year}"


class Sensor(models.Model):
    type = models.CharField(max_length=255)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.PROTECT, related_name='sensors')
    installed_date = models.DateField()

    def __str__(self):
        return self.type

    class Meta:
        indexes = [
            models.Index(fields=['vehicle_id', 'installed_date'])
        ]


class SensorValue(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.PROTECT, related_name='sensor_values')
    value = models.FloatField()
    timestamp = models.DateTimeField()


class Maintenance(models.Model):
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.PROTECT, related_name='maintenances')
    service_type = models.CharField(max_length=255)
    scheduled_date = models.DateField()

    def __str__(self):
        return self.service_type


class ServiceCenter(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    rating = models.FloatField()

    def __str__(self):
        return self.name