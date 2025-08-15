from django.contrib import admin

from JOBS_TUNE_automations.models import MailAutomation

# Register your models here.


admin.site.register(
    [
        MailAutomation,
    ]
)
