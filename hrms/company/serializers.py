from rest_framework import serializers
from .models import Company, Department
from account.serializers import UserSerializer


class CompanySerializer(serializers.ModelSerializer):
    company_employees = UserSerializer(many=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'website', 'company_employees', 'departments']
        depth = 1


class DepartmentSerializer(serializers.ModelSerializer):
    department_employees = UserSerializer(many=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'company', 'department_employees']
        depth = 1
