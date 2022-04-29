from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from .forms import UserChangeForm, UserCreationForm
from .models import DoctorMore, Doctor

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

# register doctor model
admin.site.register(Doctor)