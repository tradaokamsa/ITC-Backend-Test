from django.contrib import admin
from .models import CommitteeOfficer

# Register your models here.
class CommitteeOfficerAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'year', 'hobby']
admin.site.register(CommitteeOfficer, CommitteeOfficerAdmin)