from django.contrib import admin
from company.models import Company, Department

# Register your models here.
admin.site.register(Company)
admin.site.register(Department)


# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ['name', 'website']
