from django.urls import include, path

urlpatterns = [
    path("auth/", include("JOBS_TUNE_api.api_urls.auth.urls")),
    path("asset/", include("JOBS_TUNE_api.api_urls.asset.urls")),
    path("base/", include("JOBS_TUNE_api.api_urls.base.urls")),
    path("employee/", include("JOBS_TUNE_api.api_urls.employee.urls")),
    path("notifications/", include("JOBS_TUNE_api.api_urls.notifications.urls")),
    path("payroll/", include("JOBS_TUNE_api.api_urls.payroll.urls")),
    path("attendance/", include("JOBS_TUNE_api.api_urls.attendance.urls")),
    path("leave/", include("JOBS_TUNE_api.api_urls.leave.urls")),
]
