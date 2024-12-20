# Generated by Django 5.1.4 on 2024-12-12 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('installed_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField()),
                ('vin', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=1, max_digits=5)),
                ('timestamp', models.DateTimeField()),
                ('sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sensor_values', to='auto_tech.sensor')),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='vehicle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sensors', to='auto_tech.vehicle'),
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=255)),
                ('scheduled_date', models.DateField()),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='maintenances', to='auto_tech.vehicle')),
            ],
        ),
        migrations.AddIndex(
            model_name='sensor',
            index=models.Index(fields=['vehicle_id', 'installed_date'], name='auto_tech_s_vehicle_25686b_idx'),
        ),
    ]
