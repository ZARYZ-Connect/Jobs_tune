"""
JOBS_TUNE_automations/filters.py
"""

from JOBS_TUNE.filters import JOBS_TUNEFilterSet, django_filters
from JOBS_TUNE_automations.models import MailAutomation


class AutomationFilter(JOBS_TUNEFilterSet):
    """
    AutomationFilter
    """

    search = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = MailAutomation
        fields = "__all__"
