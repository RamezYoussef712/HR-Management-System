from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import action
from .models import Company, Department
from .serializers import CompanySerializer, DepartmentSerializer

# class CompanyViewSet(viewsets.ModelViewSet):
#     serializer_class = CompanySerializer
#     queryset = Company.objects.all()


class CompanyViewSet(viewsets.ViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
    
    def list(self, request):
        serializer = CompanySerializer(self.queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        company = get_object_or_404(self.queryset, pk=pk)
        serializer = CompanySerializer(instance=company)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        company = get_object_or_404(self.queryset, pk=pk)
        request_data = request.data
        serializer = CompanySerializer(instance=company, data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        company = get_object_or_404(self.queryset, pk=pk)
        company.delete()
        return Response(data='Resource deleted successfully', status=status.HTTP_204_NO_CONTENT)


# class DepartmentViewSet(viewsets.ModelViewSet):
#     serializer_class = DepartmentSerializer
#     queryset = Department.objects.all()
    
class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAdminUser]
    
    def list(self, request):
        serializer = DepartmentSerializer(self.queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        department = get_object_or_404(self.queryset, pk=pk)
        serializer = DepartmentSerializer(instance=department)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        department = get_object_or_404(self.queryset, pk=pk)
        request_data = request.data
        serializer = DepartmentSerializer(instance=department, data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        department = get_object_or_404(self.queryset, pk=pk)
        department.delete()
        return Response(data='Resource deleted successfully', status=status.HTTP_204_NO_CONTENT)
