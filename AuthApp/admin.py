from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeAdminForm

# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'nome', 'sobrenome', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('nome','sobrenome')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome','sobrenome', 'password1', 'password2'),
        }),
    )
    search_fields = ('email','nome','sobrenome')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
