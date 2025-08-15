"""
JOBS_TUNE_widget/urls.py
"""

from django.urls import path

from JOBS_TUNE_widgets import views

urlpatterns = [
    path("get-filter-form", views.get_filter_form, name="get-filter-form"),
]
