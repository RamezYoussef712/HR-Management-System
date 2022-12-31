from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import action
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer, LeaveRequestStateSerializer


class LeaveRequestViewSet(viewsets.ViewSet):
    serializer_class = LeaveRequestSerializer
    queryset = LeaveRequest.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def list(self, request):
        serializer = LeaveRequestSerializer(self.queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        leave_request = get_object_or_404(self.queryset, pk=pk)
        serializer = LeaveRequestSerializer(instance=leave_request)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = LeaveRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        leave_request = get_object_or_404(self.queryset, pk=pk)
        request_data = request.data
        serializer = LeaveRequestSerializer(instance=leave_request, data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        leave_request = get_object_or_404(self.queryset, pk=pk)
        leave_request.delete()
        return Response(data='Resource deleted successfully', status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_leave_requests(self, request):
        leave_requests = LeaveRequest.objects.filter(user=request.user.pk)
        serializer = LeaveRequestSerializer(instance=leave_requests, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

