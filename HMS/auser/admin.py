from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .forms import UserChangeForm, UserCreationForm
from .models import (
    DoctorMore, Doctor,
    Nurse,
    Laboratorist, Receptionist,
    Admin, LaboratoristMore,
    ReceptionistMore, AdminMore,
    NurseMore,
)
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'type')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add list filter
    list_filter = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add search fields
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # add fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'type')}
        ),
    )    

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


# Laboratoristmore signup form
@admin.register(LaboratoristMore)
class LaboratoristMoreAdmin(admin.ModelAdmin):
    list_display = ['User']
    list_filter = ['User']
    search_fields = ['User']



class ReceptionistAdmin(UserAdmin):
    # add fields
    fieldsets = (
        (None, {'fields': ('username', 'password', 'type')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add list filter
    list_filter = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add search fields
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # add fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email')}
        ),
    )

class DoctorAdmin(UserAdmin):
    # add fields
    fieldsets = (
        (None, {'fields': ('username', 'password', 'type')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add list filter
    list_filter = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add search fields
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # add fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email')}
        ),
    )

class NurseAdmin(UserAdmin):
    # add fields
    fieldsets = (
        (None, {'fields': ('username', 'password', 'type')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add list filter
    list_filter = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add search fields
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # add fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email')}
        ),
    )


class LaboratoristAdmin(UserAdmin):
    # add fields
    fieldsets = (
        (None, {'fields': ('username', 'password', 'type')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add list filter
    list_filter = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add search fields
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # add fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email')}
        ),
    )

class AdminAdmin(UserAdmin):
    # add fields
    fieldsets = (
        (None, {'fields': ('username', 'password', 'type')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add list filter
    list_filter = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # add search fields
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # add fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email')}
        ),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Receptionist, ReceptionistAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(Laboratorist, LaboratoristAdmin)
admin.site.register(Admin, AdminAdmin)


