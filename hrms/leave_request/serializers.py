from rest_framework import serializers
from .models import LeaveRequest


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'reason', 'state', 'user']


class LeaveRequestStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ['state']
