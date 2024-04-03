from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm 

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'nickname',
        'age',
        'is_staff',
        'id',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields" : ('age', 'nickname')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields" : ('age', 'nickname')}),)

admin.site.register(CustomUser, CustomUserAdmin)