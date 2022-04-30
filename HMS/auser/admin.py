from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from .forms import UserChangeForm, UserCreationForm
from .models import (
    DoctorMore, Doctor,
    Nurse, Patient,
    Laboratorist, Receptionist,
    Admin, LaboratoristMore,
    ReceptionistMore, AdminMore,
    NurseMore, PatientMore,
)

User = get_user_model()

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("type",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "is_superuser"]
    search_fields = ["username"]

# doctormore signup form
@admin.register(DoctorMore)
class DoctorMoreAdmin(admin.ModelAdmin):
    list_display = ['User']
    list_filter = ['User']
    search_fields = ['User']

# nursemore signup form
@admin.register(NurseMore)
class NurseMoreAdmin(admin.ModelAdmin):
    list_display = ['User']
    list_filter = ['User']
    search_fields = ['User']

# receptionistmore signup form
@admin.register(ReceptionistMore)
class ReceptionistMoreAdmin(admin.ModelAdmin):
    list_display = ['User']
    list_filter = ['User']
    search_fields = ['User']

# adminmore signup form
@admin.register(AdminMore)
class AdminMoreAdmin(admin.ModelAdmin):
    list_display = ['User']
    list_filter = ['User']
    search_fields = ['User']

# patientmore signup form
@admin.register(PatientMore)
class PatientMoreAdmin(admin.ModelAdmin):
    list_display = ['User']
    list_filter = ['User']
    search_fields = ['User']

# Laboratoristmore signup form
@admin.register(LaboratoristMore)
class LaboratoristMoreAdmin(admin.ModelAdmin):
    list_display = ['User']
    list_filter = ['User']
    search_fields = ['User']


@admin.register(Doctor)
class DoctorMoreAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_filter = ['username']
    search_fields = ['username']

@admin.register(Nurse)
class NurseMoreAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_filter = ['username']
    search_fields = ['username']

@admin.register(Patient)
class PatientMoreAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_filter = ['username']
    search_fields = ['username']

@admin.register(Laboratorist)
class LaboratoristMoreAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_filter = ['username']
    search_fields = ['username']

@admin.register(Receptionist)
class ReceptionistMoreAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_filter = ['username']
    search_fields = ['username']

@admin.register(Admin)
class AdminMoreAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_filter = ['username']
    search_fields = ['username']
