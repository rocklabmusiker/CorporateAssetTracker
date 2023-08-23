from rest_framework import generics, serializers, response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Company, Device, Employee, DeviceAssignment
from .serializers import (
    CompanySerializer, DeviceSerializer, EmployeeSerializer, DeviceAssignmentSerializer
)
from django.contrib.auth import get_user_model


# User Related Views and Serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class UserAPIView(generics.RetrieveAPIView):
    """API view to retrieve authenticated user details."""
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# Base View for commonly used configurations

class BaseAPIView:
    permission_classes = [IsAuthenticated]


class AdminBaseAPIView(BaseAPIView):
    permission_classes = BaseAPIView.permission_classes + [IsAdminUser]


# Company Views and Serializers

class CompanyListCreateView(BaseAPIView, generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyRetrieveUpdateDestroyView(AdminBaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# Device Views and Serializers

class DeviceListCreateView(BaseAPIView, generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceRetrieveUpdateDestroyView(AdminBaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceAssignView(AdminBaseAPIView, generics.UpdateAPIView):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer


# Employee Views and Serializers

class EmployeeListCreateView(BaseAPIView, generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroyView(AdminBaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeAssignmentsListView(BaseAPIView, generics.ListAPIView):
    serializer_class = DeviceAssignmentSerializer

    def get_queryset(self):
        employee_id = self.kwargs['pk']
        return DeviceAssignment.objects.filter(employee=employee_id)
