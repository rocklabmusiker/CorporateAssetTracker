from rest_framework import serializers
from .models import Company, Device, Employee, DeviceAssignment


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for Company model.
    """
    class Meta:
        model = Company
        fields = ('id', 'name', 'location', 'phone_number')  # Assuming these are your model fields


class DeviceSerializer(serializers.ModelSerializer):
    """
    Serializer for Device model.
    """
    class Meta:
        model = Device
        fields = ('id', 'name', 'serial_number', 'condition', 'company', 'checked_out')  # Assuming these are your model fields


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for Employee model.
    """
    class Meta:
        model = Employee
        fields = '__all__'  # Assuming these are your model fields


class DeviceAssignmentSerializer(serializers.ModelSerializer):
    """
    Serializer for DeviceAssignment model. Contains nested representations of Device and Employee.
    """
    device = DeviceSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = DeviceAssignment
        fields = ('id', 'device', 'employee', 'assigned_date', 'return_date', 'updated_at')  # Assuming these are your model fields
