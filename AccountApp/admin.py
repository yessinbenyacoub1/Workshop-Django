from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Doctor, Patient, Specialty, User

admin.site.register(User, UserAdmin)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('license_number', 'last_name', 'first_name', 'email', 'phone')
    search_fields = ('license_number', 'last_name', 'first_name')
    filter_horizontal = ('specialties',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('license_number',)
        return ()


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('national_id', 'last_name', 'first_name', 'phone', 'birth_date')
    search_fields = ('national_id', 'last_name', 'first_name')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('national_id',)
        return ()
