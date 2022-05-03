from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import (
    Director, DoctorMore, Doctor,
    Nurse,
    Laboratorist, Receptionist,
    HospitalManager, LaboratoristMore,
    ReceptionistMore, HospitalManagerMore,
    NurseMore,
)
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User = get_user_model()

class CustomUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False


    class Meta:
        model = User
        fields = ('username',)


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)

        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()
    # password change field

    class Meta:
        model = User
        fields = ('username',)


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    # form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_active',)
    # list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','type', 'email')}),
        ('Permissions', {'fields': ('is_superuser','groups')}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'type',),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = (['groups',])
    readonly_fields = ('username', 'type',)

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

# hospitalmanagermore signup form
@admin.register(HospitalManagerMore)
class HospitalManagerMoreAdmin(admin.ModelAdmin):
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
    add_form = CustomUserCreationForm
    model = Receptionist
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
            'fields': ('email',)}
        ),
    )
    readonly_fields = ('username','type',)

class DoctorAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Doctor
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
            'fields': ('email',)}
        ),
    )
    readonly_fields = ('username','type',)

class DirectorAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Director
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
            'fields': ('email',)}
        ),
    )
    readonly_fields = ('username','type',)

class HospitalManagerAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = HospitalManager
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
            'fields': ('email',)}
        ),
    )
    readonly_fields = ('username','type',)

class NurseAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Nurse
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
    exclude = ('password1','password2',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',)}
        ),
    )
    readonly_fields = ('username','type',)

class LaboratoristAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Laboratorist
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
            'fields': ('email',)}
        ),
    )
    readonly_fields = ('username', 'type',)



admin.site.register(User, CustomUserAdmin)
admin.site.register(Receptionist, ReceptionistAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Laboratorist, LaboratoristAdmin)
admin.site.register(HospitalManager, HospitalManagerAdmin)

admin.site.site_header = 'Hospital Admin'
admin.site.site_title = 'Hospital Management Platform'
admin.site.index_title = 'Hospital Administration'
