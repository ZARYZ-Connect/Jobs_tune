from django.apps import AppConfig


class JOBS_TUNEApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "JOBS_TUNE_api"

    def ready(self):
        from django.urls import include, path

        from JOBS_TUNE.urls import urlpatterns

        urlpatterns.append(
            path("api/", include("JOBS_TUNE_api.urls")),
        )
        super().ready()
