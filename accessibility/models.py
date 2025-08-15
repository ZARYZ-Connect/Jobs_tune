"""
accessibility/models.py
"""

from django.db import models

from accessibility.accessibility import ACCESSBILITY_FEATURE
from employee.models import Employee
from JOBS_TUNE.models import JOBS_TUNEModel


class DefaultAccessibility(JOBS_TUNEModel):
    """
    DefaultAccessibilityModel
    """

    feature = models.CharField(max_length=100, choices=ACCESSBILITY_FEATURE)
    filter = models.JSONField()
    exclude_all = models.BooleanField(default=False)
    employees = models.ManyToManyField(
        Employee, blank=True, related_name="default_accessibility"
    )
    is_enabled = models.BooleanField(default=True)
