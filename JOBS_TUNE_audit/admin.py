"""
admin.py
"""

from django.contrib import admin

from JOBS_TUNE_audit.models import AuditTag, JOBS_TUNEAuditInfo, JOBS_TUNEAuditLog

# Register your models here.

admin.site.register(AuditTag)
