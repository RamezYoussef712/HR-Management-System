from django.contrib.auth.models import AbstractUser
from django.db import models
from company.models import Company, Department


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee')
    )
    STATE_CHOICES = (
        ('active', 'Active'),
        # ('inactive', 'Inactive'),
        ('terminated', 'Terminated')
    )

    hire_date = models.DateField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    company = models.ForeignKey(Company, related_name='company_employees', on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, related_name='department_employees', on_delete=models.CASCADE, null=True)

    # User Overriden fields:
    is_active = models.CharField(max_length=20, choices=STATE_CHOICES, default='active')

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username
