from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# Step 1: Unregister the default UserAdmin
admin.site.unregister(User)

# Step 2: Define your custom admin class
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', 'password']

# Step 3: Register the User model with your custom admin class
admin.site.register(User, CustomUserAdmin)
