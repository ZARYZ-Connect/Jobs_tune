"""
App configuration for the JOBS_TUNE Automations app.
Initializes model choices and starts automation when the server runs.
"""

import os
import sys

from django.apps import AppConfig


class JOBS_TUNEAutomationConfig(AppConfig):
    """Configuration class for the JOBS_TUNE Automations Django app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "JOBS_TUNE_automations"

    def ready(self):
        """Run initialization tasks when the app is ready."""
        from base.templatetags.JOBS_TUNEfilters import app_installed
        from employee.models import Employee
        from JOBS_TUNE_automations.methods.methods import get_related_models
        from JOBS_TUNE_automations.models import MODEL_CHOICES as model_choices

        # Build MODEL_CHOICES
        models = [Employee]
        if app_installed("recruitment"):
            from recruitment.models import Candidate

            models.append(Candidate)

        for main_model in models:
            for model in get_related_models(main_model):
                model_choices.append(
                    (f"{model.__module__}.{model.__name__}", model.__name__)
                )

        model_choices.append(("employee.models.Employee", "Employee"))
        model_choices.append(("pms.models.EmployeeKeyResult", "Employee Key Results"))
        model_choices[:] = list(set(model_choices))  # Update in-place

        # Only start automation when running the server
        if (
            len(sys.argv) >= 2
            and sys.argv[1] == "runserver"
            and os.environ.get("RUN_MAIN") == "true"
        ):
            from JOBS_TUNE_automations.signals import start_automation

            start_automation()
