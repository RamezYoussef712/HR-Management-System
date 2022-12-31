from django.db import models
from account.models import User


class LeaveRequest(models.Model):
    STATE_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined')
    )

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    reason = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='pending')
    user = models.ForeignKey(User, related_name='employee', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.reason + '-' + str(self.end_date)
