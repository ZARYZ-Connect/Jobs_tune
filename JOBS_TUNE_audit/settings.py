"""
JOBS_TUNE_audit/settings.py

This module is used to write settings contents related to payroll app
"""

from JOBS_TUNE.settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "JOBS_TUNE_audit.context_processors.history_form",
)
