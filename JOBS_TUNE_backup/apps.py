from django.apps import AppConfig


class BackupConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "JOBS_TUNE_backup"

    def ready(self):
        from django.urls import include, path

        from JOBS_TUNE.urls import urlpatterns

        urlpatterns.append(
            path("backup/", include("JOBS_TUNE_backup.urls")),
        )
        super().ready()
