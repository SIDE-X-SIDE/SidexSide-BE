from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User
from .models import *



# Register your models here.
# class ProfileLInline(admin.StackedInline):
#     model = Profile
#     can_delete: bool = False
#     verbose_name_plural = 'profile'

# class UserAdmin(BaseUserAdmin):
#     inline = (ProfileLInline,)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)