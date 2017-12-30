from django.apps import AppConfig
from django.contrib import admin

from .models import Employee


class EmployeeModelAdmin(admin.ModelAdmin):
	list_display = ["id", "firstName", "lastName" ,"slug", "email", "mobileNumber"]
	list_display_links = ["slug"]
	list_editable = ["firstName"]
	list_filter = ["featured", ]

	search_fields = ["firstName", "slug"]
	class Meta:
		model = Employee


admin.site.register(Employee, EmployeeModelAdmin)






