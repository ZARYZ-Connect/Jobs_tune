from django.apps import AppConfig


class OnboardingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "onboarding"

    def ready(self):
        from django.urls import include, path

        from JOBS_TUNE.JOBS_TUNE_settings import APPS
        from JOBS_TUNE.urls import urlpatterns

        APPS.append("onboarding")
        urlpatterns.append(
            path("onboarding/", include("onboarding.urls")),
        )
        super().ready()
