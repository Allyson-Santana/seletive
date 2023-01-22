from django.contrib import admin

from .models import Technology, Company, Job

admin.site.register(Technology)
admin.site.register(Company)
admin.site.register(Job)