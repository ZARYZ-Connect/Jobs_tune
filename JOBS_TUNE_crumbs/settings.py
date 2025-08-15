from JOBS_TUNE.settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "JOBS_TUNE_crumbs.context_processors.breadcrumbs",
)
