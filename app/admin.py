from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserRole)
admin.site.register(RoleType)
admin.site.register(UserDetail)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(School)
admin.site.register(School_post)
admin.site.register(Car_brand_model)
admin.site.register(Car_brand)


