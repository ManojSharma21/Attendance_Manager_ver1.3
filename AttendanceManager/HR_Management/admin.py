from .models import Employees_Detail
from .models import Daily_Attendance
from django.contrib import admin
from .models import Employee_Payroll
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class UserProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("Employee_Id","Time_in","Time_out","Status")
    list_filter = ("Time_in",)
admin.site.register(Employees_Detail)
admin.site.register(Daily_Attendance,UserProfileAdmin)
admin.site.register(Employee_Payroll)