from django.db import models


# Company
class Company(models.Model):
    name = models.CharField(max_length=30, unique=True)
    website = models.URLField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=30, unique=True)
    company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


