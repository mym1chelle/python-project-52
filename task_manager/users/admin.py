from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from task_manager.users.models import Users

admin.site.register(Users, UserAdmin)
