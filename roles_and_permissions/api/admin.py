from django.contrib import admin
from . models import Permission, Role, UserRole

# Register your models here.
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(UserRole)